import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)



CSV_FILE_PATH = get_path(filename="books.csv")
JSON_FILE_PATH = get_path(filename="users.json")
JSON_RESULT_FILE_PATH = get_path(filename="result.json")
JSON_BOOKS_FILE_PATH = get_path(filename="books.json")
# XML_FILE_PATH = get_path(filename="books.xml")
# JPEG_FILE_PATH = get_path(filename="example.jpeg")
# TXT_FILE_PATH = get_path(filename="example.txt")