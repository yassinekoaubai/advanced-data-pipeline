from base import FileParser
import csv
import os

class ParseCsv(FileParser):
    def parse_file(self, path):
        file_path = os.path.expanduser(path)
        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            return [row for row in reader]
