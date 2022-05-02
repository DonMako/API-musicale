import requests


def recup_lyrics(nom_artiste: str, title: str):
    requete = requests.get(
        "https://api.lyrics.ovh/v1/" + str(nom_artiste) + "/" + str(title)
    )
    return requete["lyrics"]
