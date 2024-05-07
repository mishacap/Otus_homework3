import json
from files import JSON_BOOKS_FILE_PATH
from files import JSON_RESULT_FILE_PATH


with open(JSON_RESULT_FILE_PATH, "r") as users:
    data_users = json.load(users)

with open(JSON_BOOKS_FILE_PATH, "r") as books:
    data_books = json.load(books)

book_index = 0

for user in data_users[:14]:
    books_array = user["books"]
    books_to_move = data_books[book_index:book_index + 8]
    books_array.extend(books_to_move)
    book_index += 8

for user in data_users[14:]:
    books_array = user["books"]
    books_to_move = data_books[book_index:book_index + 7]
    books_array.extend(books_to_move)
    book_index += 7

with open(JSON_RESULT_FILE_PATH, "w") as users_file:
    json.dump(data_users, users_file, indent=4)
