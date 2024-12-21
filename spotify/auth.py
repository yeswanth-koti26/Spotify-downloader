import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
SPOTIFY_CLIENT_ID = "2f5091f611714d598b169efa72ea3091"
SPOTIFY_CLIENT_SECRET = "8ae7e0c6d6334cf5a62cb3283dcca9c8"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-read-private"
    ))
