import json
import requests
from client.totalScore import totalScore
from client.addNumberSearches import addNumberSearches


def getPlaylist(file: json, len_playlist: int) -> None:
    with open(str(file), "r") as read_file:
        data = json.load(read_file)
    total_score = totalScore(data)
    addNumberSearches(data, total_score, len_playlist)
    playlist = []
    for artist in data:
        for i in range(artist["numberSearches"]):
            requete = requests.get(os.getenv("url_server")+"/random/"+artist['artiste']).json()
            playlist.append(requete)
    data_file = open("playlist.json", "w")
    json.dump(playlist, data_file, indent="")
    return playlist
