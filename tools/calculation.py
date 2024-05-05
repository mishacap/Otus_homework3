import json
from csv import DictReader
from files import CSV_FILE_PATH
from files import JSON_RESULT_FILE_PATH

with open(JSON_RESULT_FILE_PATH, "r") as json_file:
    data = json.load(json_file)

num_users = len(data)

with open(CSV_FILE_PATH, "r") as csv_file:
    data = DictReader(csv_file)
    num_books = 0
    for row in data:
        num_books +=1


