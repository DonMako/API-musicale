import requests
from typing import List


def getTracksAlbum(id_album: int) -> List[dict]:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/track.php?m=" + str(
            id_album)
    )
    list_info_tracks = requete["track"]
    list_tracks = []
    for track in list_info_tracks:
        dico = {}
        dico["id_track"] = track["idTrack"]
        dico["title"] = track["strTrack"]
        list_tracks.append(dico)
    return list_tracks
