import requests


def getIdArtist(nom_artiste: str):
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/2/search.php?s=" + nom_artiste)
    return requete["artists"][0]["idArtist"]
