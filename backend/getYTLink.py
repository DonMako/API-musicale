import requests


def getYTLink(idArtist: int, idTrack: int):
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/mvid.php?i=" + str(
            idArtist)
    )
    liste_liens = requete["mvids"]
    for i in len(liste_liens):
        if liste_liens["idTrack"] == idTrack:
            return liste_liens["strMusicVid"]
