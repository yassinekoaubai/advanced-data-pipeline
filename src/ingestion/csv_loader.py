import csv
import os

path = os.path.expanduser("~/Documents/advance_data_pipeline/data/raw/Orders.csv")

def read_csv(path):
    with open(path) as csv_file:
        data = []
        reader = csv.DictReader(csv_file)
        for i in reader:
            data.append(i)
        return data

