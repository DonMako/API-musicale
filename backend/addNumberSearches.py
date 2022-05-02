import json
from backend.totalScore import totalScore


def addNumberSearches(file: json, len_playlist: int):
    total_score = totalScore(file)
    for i in len(file):
        file[i]["numberSearches"] = round(
            file[i]["note"]/total_score*len_playlist)
