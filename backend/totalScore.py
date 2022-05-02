import json


def totalScore(file: json):
    total = 0
    for i in len(file):
        total += file[i]["note"]
    return total
