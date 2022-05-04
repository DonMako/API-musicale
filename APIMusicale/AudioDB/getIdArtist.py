import json
import requests


def getIdArtist(name_artist: str) -> int:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/2/search.php?s=" + name_artist).json()
    data = json.load(open(requete, "r"))
    return data["artists"][0]["idArtist"]
