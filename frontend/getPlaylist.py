import json
from backend.createPlaylist import createPlaylist


def getPlaylist(file: json, len_playlist: int) -> json:
    return createPlaylist(file, len_playlist)
