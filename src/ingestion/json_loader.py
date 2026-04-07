import json
import os

file_path = os.path.expanduser("~/Documents/advance_data_pipeline/data/raw/Orders.json")
with open(file_path, mode="r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    print(data)