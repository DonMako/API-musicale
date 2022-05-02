import json
from backend.totalScore import totalScore


def addNumberSearches(len_playlist: int, file: json):
    total_score = totalScore(file)
    for i in len(file):
        file[i]["numberSearches"] = round(
            file[i]["note"]/total_score*len_playlist)
