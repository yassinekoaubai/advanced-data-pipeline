from base import FileParser
import json
import os

class ParseJson(FileParser):
    def parse_file(self, path):
        file_path = os.path.expanduser(path)
        with open(file_path, mode="r", encoding="utf-8") as json_file:
            return json.load(json_file)