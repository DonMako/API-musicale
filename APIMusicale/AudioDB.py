import requests
from typing import List


def getIdDiscography(id_artist: int) -> List[int]:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/album.php?i=" + str(
            id_artist)
    ).json
    list_albums = requete["album"]
    list_id_albums = []
    for album in list_albums:
        list_id_albums.append(album["idAlbum"])
    return list_id_albums

def getIdArtist(name_artist: str) -> int:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/2/search.php?s=" + name_artist
    ).json()
    return requete["artists"][0]["idArtist"]
    
def getTracksAlbum(id_album: int) -> List[dict]:
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/track.php?m=" + str(
            id_album)
    ).json()
    list_info_tracks = requete["track"]
    list_tracks = []
    for track in list_info_tracks:
        dico = {}
        dico["id_track"] = track["idTrack"]
        dico["title"] = track["strTrack"]
        list_tracks.append(dico)
    return list_tracks
    
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