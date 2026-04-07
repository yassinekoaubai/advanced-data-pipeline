import os
import xml

file_path = os.path.expanduser("~/Documents/advance_data_pipeline/data/raw/Orders.xml")
with open(file_path, encoding="utf-8") as xml_file:
    data = xml_file.read()
    print(data)