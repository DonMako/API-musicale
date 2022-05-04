from typing import List
from APIMusicale.AudioDB.getIdArtist import getIdArtist
from APIMusicale.AudioDB.getIdDiscography import getIdDiscography
from APIMusicale.AudioDB.getTracksAlbum import getTracksAlbum


def getTracksArtist(name_artist: str) -> List[dict]:
    id_artist = getIdArtist(name_artist)
    list_id_albums = getIdDiscography(id_artist)
    list_tracks = []
    for id_album in list_id_albums:
        list_tracks = list_tracks + getTracksAlbum(id_album)
    return list_tracks
