import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    new_data = []

    with open(INPUT_FILENAME, encoding="utf-8") as i:
        reader = csv.DictReader(i)
        [new_data.append(row) for row in reader]

    with open(OUTPUT_FILENAME, 'w') as o:
        json.dump(new_data, o, indent=4)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
