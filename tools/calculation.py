import json
from files import JSON_RESULT_FILE_PATH

with open(JSON_RESULT_FILE_PATH, "r") as json_file:
    data = json.load(json_file)

num_users = len(data)

