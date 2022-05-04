import json
import requests
from typing import List


def getIdDiscography(id_artist: int) -> List[int]:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/album.php?i=" + str(
            id_artist)
    ).json
    data = json.load(open(requete, "r"))
    list_albums = data["album"]
    list_id_albums = []
    for album in list_albums:
        list_id_albums.append(album["idAlbum"])
    return list_id_albums
