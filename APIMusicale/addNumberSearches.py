import json
from APIMusicale.totalScore import totalScore


def addNumberSearches(file: json, len_playlist: int) -> None:
    with open(str(file), "r") as read_file:
        data = json.load(read_file)
    total_score = totalScore(data)
    for dico in data:
        dico["numberSearches"] = round(
            dico["note"]/total_score*len_playlist)
