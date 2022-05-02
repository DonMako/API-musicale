import requests


def getLyricsSong(name_artist: str, title: str) -> str:
    requete = requests.get(
        "https://api.lyrics.ovh/v1/" + name_artist + "/" + title
    )
    return requete["lyrics"]
