def totalScore(data: dict) -> int:
    total = 0
    for i in range(len(data)):
        total += data[i]["note"]
    return total
