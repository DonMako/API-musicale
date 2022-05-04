import json
import requests
from typing import List
from client.createPlaylist.totalScore import totalScore
from client.createPlaylist.addNumberSearches import addNumberSearches


def getPlaylist(file: json, len_playlist: int) -> List[dict]:
    with open(str(file), "r") as read_file:
        data = json.load(read_file)
    total_score = totalScore(data)
    addNumberSearches(data, total_score, len_playlist)
    playlist = []
    for artist in data:
        for i in range(artist["numberSearches"]):
            track = requests.get(
                "http://127.0.0.1:8000/random/" + artist["artiste"]
            )
            playlist.append(track)
    data_file = open("playlist.json", "w")
    json.dump(playlist, data_file, indent="")
    return playlist
