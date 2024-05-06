import csv
import json
from files import CSV_FILE_PATH
from files import JSON_BOOKS_FILE_PATH

csv_data = []

with open(CSV_FILE_PATH, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data.append(row)

with open(JSON_BOOKS_FILE_PATH, "w") as json_file:
    json.dump(csv_data, json_file, indent=4)
