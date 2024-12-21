from youtubesearchpython import VideosSearch

def search_youtube(song_title):
    search = VideosSearch(song_title, limit=1)
    return search.result()['result'][0]['link']
