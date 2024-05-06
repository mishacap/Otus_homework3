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
Convert the books.csv file to a books.json file and remove the extra lines
"""
csv_data = []
with open(CSV_FILE_PATH, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if all(key in row for key in ["title", "author", "pages", "genre"]):
            csv_data.append({
                "title": row["title"],
                "author": row["author"],
                "pages": row["pages"],
                "genre": row["genre"]
            })
print(csv_data)