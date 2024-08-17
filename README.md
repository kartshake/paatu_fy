## Paatu_fy the Spotify downloader

**Paatu_fy** is a Python program that downloads your tracks or even entire playlists.
It works by fetching your Spotify track or playlist url, then using Spotify's API it gathers the track/playlist data, searches the song(s) on YouTube, and downloads it/them using Google's YOUTUBE API.

## Installation

1. Clone the repository:
  - (https://github.com/kartshake/paatu_fy.git)
2. Install dependencies:
  - pip install -r requirements.txt

## Configuration

Before using the program, you need to set up your Spotify and Google API credentials:

1. Obtain Spotify API credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Obtain Google's Youtube DATA API key from the [Google Cloud Console](https://console.cloud.google.com/).
3. Set up the required environment variables or configuration files with your API keys.

## API Documentation

- [Spotify API Documentation](https://developer.spotify.com/documentation/web-api/)
- [Google API Documentation](https://developers.google.com/youtube/v3/getting-started)

## Running the Program
1. Run the **paatu_fy.py** file.
2.  Paste your track/playlist url.
3. Click ENTER, sit back and relax while your tracks get downloaded.

## Credits

- Thanks to the Spotify and Google APIs for providing the necessary functionalities.
- Special thanks to Rockstar Games for the inspiration behind this project.
- Special thanks to SYNSATION(https://www.youtube.com/@synsation) for the video that helped me understand spotify OAuth.
