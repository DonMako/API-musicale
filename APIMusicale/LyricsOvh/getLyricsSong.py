import json
import requests


def getLyricsSong(name_artist: str, title: str) -> str:
    requete = requests.get(
        "https://api.lyrics.ovh/v1/" + name_artist + "/" + title
    ).json()
    data = json.load(open(requete, "r"))
    return data["lyrics"]
