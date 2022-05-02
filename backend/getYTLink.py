import requests
from backend.getIdArtist import getIdArtist


def getYTLink(name_artist: str, id_track: int):
    id_artist = getIdArtist(name_artist)
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/mvid.php?i=" + str(
            id_artist)
    )
    liste_liens = requete["mvids"]
    for i in len(liste_liens):
        if liste_liens["idTrack"] == id_track:
            return liste_liens["strMusicVid"]
        else:
            return "Pas de lien YT pour cette musique"
