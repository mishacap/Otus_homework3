from csv import DictReader
from files import CSV_FILE_PATH

with open(CSV_FILE_PATH, newline='') as csv_file:
    reader = DictReader(csv_file)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
