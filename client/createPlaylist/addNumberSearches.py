from typing import List


def addNumberSearches(data: List[dict], total_score: int, len_playlist: int):
    for dico in data:
        dico["numberSearches"] = round(
            dico["note"]/total_score*len_playlist)
    return data
