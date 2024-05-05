import json
from files import JSON_FILE_PATH

with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

users_list = users

for user in users_list:
    print(user)