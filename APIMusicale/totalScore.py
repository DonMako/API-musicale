from typing import List


def totalScore(data: List[dict]) -> int:
    total = 0
    for dico in data:
        total += dico["note"]
    return total
