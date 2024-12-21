def fetch_playlist_songs(sp, playlist_id):
    results = sp.playlist_items(playlist_id)
    songs = []

    for item in results['items']:
        track = item['track']
        songs.append(f"{track['name']} {track['artists'][0]['name']}")

    return songs
