from csv_loader import ParseCsv
from json_loader import ParseJson
from xml_loader import ParseXml

class Factory:
    _registry = {"csv": ParseCsv, "json": ParseJson, "xml": ParseXml}

    @classmethod
    def create(cls, fmt: str):
        cls_type = cls._registry.get(fmt)
        if not cls_type:
            raise ValueError(f"Unsupported format: {fmt}")
        return cls_type()

if __name__ == "__main__":
    parser = Factory.create("xml")
    data = parser.parse_file("/home/retard/Documents/advance_data_pipeline/data/raw/Orders.xml")
    print(data)