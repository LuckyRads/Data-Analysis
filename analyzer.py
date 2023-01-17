from abc import ABC, abstractmethod

from data_collector import DataCollector


class Analyzer(ABC):

    def __init__(self, data_collector: DataCollector):
        self._data = data_collector.get_data()

    @abstractmethod
    def transform_dataset(self):
        pass

    @abstractmethod
    def get_statistics(self, statistics_type, attributes):
        pass

    @abstractmethod
    def print_statistics(self, statistics_type, attributes, precision=2):
        pass
