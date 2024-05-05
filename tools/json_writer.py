import json
from files import JSON_RESULT_FILE_PATH

data = {}

with open(JSON_RESULT_FILE_PATH, "w") as json_result_file:
    save = json.dumps(data, indent=4)
    json_result_file.write(save)
