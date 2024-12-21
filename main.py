from spotify.auth import get_spotify_client
from utils.logger import logger

def fetch_album_songs(sp, album_id):
    # Fetch album tracks
    results = sp.album_tracks(album_id)
    songs = []

    for item in results['items']:
        track_name = item['name']
        artist_name = item['artists'][0]['name']
        songs.append(f"{track_name} {artist_name}")

    return songs

def main():
    # Spotify authentication
    logger.info("Authenticating with Spotify...")
    sp = get_spotify_client()

    # Fetch songs from album
    album_id = "5KyjKMeVIJ1vh3rlDMj4Qa"  # Extracted from the album URL
    logger.info("Fetching songs from Spotify album...")
    songs = fetch_album_songs(sp, album_id)

    # Process each song
    for song in songs:
        try:
            logger.info(f"Processing song: {song}")
            # Placeholder for YouTube search and download
            logger.info(f"Processed song successfully: {song}")
        except Exception as e:
            logger.error(f"Error processing {song}: {e}")

if __name__ == "__main__":
    main()
