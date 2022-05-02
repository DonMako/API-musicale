import requests
from backend.getIdArtist import getIdArtist
from backend.getIdDiscography import getIdDiscography


def getTracksArtist(name_artist: str):
    id_artist = getIdArtist(name_artist)
    list_id_albums = getIdDiscography(id_artist)
    list_tracks = []
    for i in len(liste_id_album):
        requete = requests.get(
            "https://theaudiodb.com/api/v1/json/{APIKEY}/track.php?m=" + str(
                liste_id_album[i])
        )
        liste_info_pistes = requete["track"]
        for j in len(liste_info_pistes):
            dico = {}
            dico["idTrack"] = liste_info_pistes[j]["idTrack"]
            dico["title"] = liste_info_pistes[j]["strTrack"]
            list_tracks.append(dico)
    return list_tracks
