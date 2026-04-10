from base import FileParser
import os
import xml.etree.ElementTree as ET

class ParseXml(FileParser):
    def parse_file(self, path):
        file_path = os.path.expanduser(path)
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = []
        for record in root:
            item = {}
            for field in record:
                item[field.tag] = field.text
            data.append(item)
        return data
