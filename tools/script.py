import json
import csv
from files import JSON_FILE_PATH
from files import JSON_BOOKS_FILE_PATH
from files import CSV_FILE_PATH
from files import JSON_RESULT_FILE_PATH


"""
Transfer the required data from the users.json file to the result.json file
"""
extracted_data = []

with open(JSON_FILE_PATH, "r") as json_file:
    json_data = json.load(json_file)
    for item in json_data:
        if all(key in item for key in ["name", "gender", "address", "age"]):
            extracted_data.append({
                "name": item["name"],
                "gender": item["gender"],
                "address": item["address"],
                "age": item["age"]
            })

with open(JSON_RESULT_FILE_PATH, "w") as json_result_file:
    json.dump(extracted_data, json_result_file, indent=4)



"""
Add an array of books for each user to result.json
"""
with open(JSON_RESULT_FILE_PATH, "r") as json_file:
    json_data = json.load(json_file)
    for item in json_data:
        if all(key in item for key in ["name", "gender", "address", "age"]):
            item["books"] = []


with open(JSON_RESULT_FILE_PATH, "w") as json_file:
    json.dump(json_data, json_file, indent=4)


"""
Convert the books.csv file to a books.json file
"""
csv_data = []

with open(CSV_FILE_PATH, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data.append(row)

with open(JSON_BOOKS_FILE_PATH, "w") as json_file:
    json.dump(csv_data, json_file, indent=4)


"""
Remove extra line from books.json
"""
extracted_data = []

with open(JSON_BOOKS_FILE_PATH, "r") as json_file:
    data = json.load(json_file)
    for item in data:
        if all(key in item for key in ["Title", "Author", "Genre", "Pages"]):
            extracted_data.append({
                "Title": item["Title"],
                "Author": item["Author"],
                "Genre": item["Genre"],
                "Pages": item["Pages"]
            })


with open(JSON_BOOKS_FILE_PATH, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)