import json


def totalScore(file: json) -> int:
    total = 0
    for i in range(len(file)):
        total += file[i]["note"]
    return total
