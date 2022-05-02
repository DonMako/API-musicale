import requests


def getTracksAlbum(id_album: int):
    list_tracks = []
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/track.php?m=" + str(
            id_album)
    )
    list_info_tracks = requete["track"]
    for j in len(list_info_tracks):
        dico = {}
        dico["id_track"] = list_info_tracks[j]["idTrack"]
        dico["title"] = list_info_tracks[j]["strTrack"]
        list_tracks.append(dico)
    return list_tracks
