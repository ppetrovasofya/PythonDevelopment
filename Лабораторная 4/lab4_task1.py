import json

INPUT = "input.json"


def task() -> float:
    with open(INPUT, encoding="utf-8") as f:
        json_data = json.load(f)
        total = sum([i["score"] * i["weight"] for i in json_data])
        return round(total, 3)


print(task())
