import requests


def getYTLink(id_artist: int, id_track: int) -> str:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/mvid.php?i=" + str(
            id_artist)
    ).json()
    liste_liens = requete["mvids"]
    for lien in liste_liens:
        if lien["idTrack"] == id_track:
            return lien["strMusicVid"]
        else:
            return "Pas de lien YT pour cette musique"
