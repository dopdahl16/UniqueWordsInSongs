import azapi

def FetchLyrics(artist, title):
    API = azapi.AZlyrics('google', accuracy=0.5)
    API.artist = artist
    API.title = title
    time.sleep(3)
    API.getLyrics(save=False)
    return API.lyrics