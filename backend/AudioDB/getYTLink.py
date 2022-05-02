import requests
from backend.AudioDB.getIdArtist import getIdArtist


def getYTLink(name_artist: str, id_track: int) -> str:
    id_artist = getIdArtist(name_artist)
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/mvid.php?i=" + str(
            id_artist)
    )
    liste_liens = requete["mvids"]
    for lien in liste_liens:
        if lien["idTrack"] == id_track:
            return lien["strMusicVid"]
        else:
            return "Pas de lien YT pour cette musique"
