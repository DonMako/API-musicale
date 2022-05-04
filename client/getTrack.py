import requests


def getTrack(name_artist: str) -> dict:
    return requests.get(
        "http://127.0.0.1:8000/random/" + name_artist
    )
