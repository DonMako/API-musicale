import requests


def getIdArtist(name_artist: str) -> int:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/2/search.php?s=" + name_artist)
    return requete["artists"][0]["idArtist"]
