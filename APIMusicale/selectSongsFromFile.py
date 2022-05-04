import json
from typing import List
from APIMusicale.AudioDB.getIdArtist import getIdArtist
from client.getRandomTrackArtist import getRandomTrackArtist


def selectSongsFromFile(file: json) -> List[dict]:
    list_songs = []
    for artist in file:
        song = getRandomTrackArtist(artist["artiste"])
        song["name_artist"] = artist["artiste"]
        song["id_artist"] = getIdArtist(artist["artiste"])
        list_songs.append(song)
    return list_songs
