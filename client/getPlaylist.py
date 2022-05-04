import json
from APIMusicale.createPlaylist import createPlaylist


def getPlaylist(file: json, len_playlist: int) -> None:
    data_file = open("playlist.json", "w")
    playlist = createPlaylist(file)
    json.dump(playlist, data_file, indent="")
    data_file.close()
