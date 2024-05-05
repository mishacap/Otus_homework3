import json
from files import JSON_FILE_PATH
from files import JSON_RESULT_FILE_PATH

extracted_data = []

with open(JSON_FILE_PATH, "r") as json_file:
    data = json.load(json_file)
    for item in data:
        if all(key in item for key in ["name", "gender", "address", "age"]):
            extracted_data.append({
                "name": item["name"],
                "gender": item["gender"],
                "address": item["address"],
                "age": item["age"]
            })


with open(JSON_RESULT_FILE_PATH, "w") as json_result_file:
    json.dump(extracted_data, json_result_file, indent=4)