import requests


def getYTLink(id_artist: int, id_track: int):
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/mvid.php?i=" + str(
            id_artist)
    )
    liste_liens = requete["mvids"]
    for i in len(liste_liens):
        if liste_liens["idTrack"] == id_track:
            return liste_liens["strMusicVid"]
