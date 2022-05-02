import json
from backend.totalScore import totalScore


def addNumberSearches(file: json, len_playlist: int) -> None:
    with open(str(file), "r") as read_file:
        data = json.load(read_file)
    total_score = totalScore(data)
    for i in range(len(data)):
        file[i]["numberSearches"] = round(
            file[i]["note"]/total_score*len_playlist)
