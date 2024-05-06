import json
from files import JSON_RESULT_FILE_PATH

with open(JSON_RESULT_FILE_PATH, "r") as json_file:
    data = json.load(json_file)
    for item in data:
        if all(key in item for key in ["name", "gender", "address", "age"]):
            item["books"] = []


with open(JSON_RESULT_FILE_PATH, "w") as json_result_file:
    json.dump(data, json_result_file, indent=4)
