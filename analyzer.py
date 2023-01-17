from abc import ABC, abstractmethod


class Analyzer(ABC):

    def __init__(self, data):
        self._data = data

    @abstractmethod
    def transform_dataset(self):
        pass
