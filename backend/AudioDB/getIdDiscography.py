import requests
from typing import List


def getIdDiscography(id_artist: int) -> List[int]:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/album.php?i=" + str(
            id_artist)
    )
    liste_info_album = requete["album"]
    list_id_albums = []
    for i in len(liste_info_album):
        list_id_albums.append(liste_info_album[i]["idAlbum"])
    return list_id_albums
