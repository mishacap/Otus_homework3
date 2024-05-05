import json
from files import JSON_FILE_PATH

with open(JSON_FILE_PATH, "r") as json_file:
    users = json.load(json_file)

users_list = users

for user in users_list:
    print(user)