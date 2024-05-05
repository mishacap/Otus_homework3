import csv
import json
from csv import DictReader
from files import CSV_FILE_PATH
from files import JSON_RESULT_FILE_PATH

csv_data = []

with open(CSV_FILE_PATH, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data.append(row)
