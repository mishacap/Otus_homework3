import json
from csv import DictReader
from files import CSV_FILE_PATH
from files import JSON_RESULT_FILE_PATH

with open(JSON_RESULT_FILE_PATH, "r") as json_file:
    data = json.load(json_file)

num_users = len(data)

with open(CSV_FILE_PATH, "r") as csv_file:
    data = DictReader(csv_file)
    num_books = 0
    for row in data:
        num_books += 1


# The first 14 users will receive 8 books each and the rest will receive 7 books each.
books_per_user = num_books // num_users
print(f"Каждому юзеру нужно раздать по {books_per_user} книг")

remainder_books = num_books % num_users
print(f"Оставшиеся {remainder_books} книг можно распределить между первыми юзерами из списка")
