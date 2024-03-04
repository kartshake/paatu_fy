import spotipy
import os
from googleapiclient.discovery import build
from pytube import YouTube
from spotipy.oauth2 import SpotifyOAuth

# set the Spotify credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'http://localhost:8080/callback'

# create a Spotipy instance
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='playlist-read-private'))

# get the tracks from the selected playlist
def get_playlist_tracks(playlist_id):
    playlist_tracks = sp.playlist_items(playlist_id)
    
    # extract track information
    tracks_info = []
    for track in playlist_tracks['items']:
        track_info = {
            'name': track['track']['name'],
            'artists': [artist['name'] for artist in track['track']['artists']],
            'album': track['track']['album']['name'],  # Album name
            'release_date': track['track']['album']['release_date'],  # Release date of the album
            'duration_ms': track['track']['duration_ms'],  # Duration of the track in milliseconds
        }
        tracks_info.append(track_info)
    
    return tracks_info

# get information about the track using track ID
def get_track_info(track_id):
    track_info = sp.track(track_id)
    
    # extract track information
    track_data = {
        'name': track_info['name'],
        'artists': [artist['name'] for artist in track_info['artists']],
        'album': track_info['album']['name'],  # Album name
        'release_date': track_info['album']['release_date'],  # Release date of the album
        'duration_ms': track_info['duration_ms'],  # Duration of the track in milliseconds
    }
    return [track_data]

# Search for a song on YouTube using the YouTube Data API
def search_youtube(query):
    api_key = 'YOUR_YOUTUBE_DATA_API'  # Replace with your own YouTube Data API key
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=5  # You can adjust this number based on your preference
    )
    response = request.execute()
    
    urls=[]
    # Extract video URL from the search results
    for item in response['items']:
         video_id = item['id']['videoId']
         video_url = f'https://www.youtube.com/watch?v={video_id}'
         urls.append(video_url)
    
    return urls

def download_audio(urls, output_path):
    try:
        yt = YouTube(urls[0])
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print("Audio downloaded successfully!\n")
    
    except Exception:
        #in case the program is unable to download the video
        print('ssss')
        files = os.listdir(output_path)
        latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(output_path, f)))
        file_path = os.path.join(output_path, latest_file)
        try:
            os.remove(file_path)
        except Exception as e:
            print("Error deleting file:", e)

        if len(urls)==1:
            print("Failed to download")
            return 
        download_audio(urls[1:],output_path)
        

def main():
    while True:
        s_url=input("Enter URL: ")
        print()
        if 'track' in s_url:
            songs_data = get_track_info(s_url)
            break
        elif 'playlist' in s_url:
            songs_data=get_playlist_tracks(s_url)
            break
        else:
            print("Enter Valid URL")
    
    
    songs=len(songs_data)
    
    if songs:
        ind=1
        for song_info in songs_data:
            print(f"[{ind}/{songs}]")
            song_title = song_info['name']
            artist = song_info['artists']
            query = f'{song_title} {artist} official music video'  # Constructing the query

            print(f"Searching for '{song_title}' by {artist} on YouTube...")
            video_urls = search_youtube(query)
            
            if len(video_urls)==0:
                print("Song not Found in YouTube")
                continue

            print(f"Downloading '{song_title}' by {artist}")
            download_audio(video_urls,'YOUR_OUTPUT_PATH') #replace with the location where you want your files to be saved
    else:
        print("No Songs Found Playlist Empty")

if __name__ == "__main__":
    main()
