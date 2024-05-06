import json
from files import JSON_BOOKS_FILE_PATH
from files import JSON_RESULT_FILE_PATH


with open(JSON_RESULT_FILE_PATH, "r") as users:
    data_users = json.load(users)

with open(JSON_BOOKS_FILE_PATH, "r") as books:
    data_books = json.load(books)

print(data_users)
# print(data_books)
# books_to_move = data_books[:8]
# print(books_to_move)


