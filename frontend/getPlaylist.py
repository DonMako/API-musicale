import json
from backend.createPlaylist import createPlaylist


def getPlaylist(file: json, len_playlist: int) -> dict:
	return createPlaylist(file, len_playlist)