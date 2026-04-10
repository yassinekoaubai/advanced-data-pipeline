from abc import ABC, abstractmethod

class FileParser(ABC):
    @abstractmethod
    def parse_file(self, path):
        pass