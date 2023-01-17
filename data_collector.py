from abc import ABC, abstractmethod

from logger import Logger


class DataCollector(ABC):

    def __init__(self, input_filepath):
        self.filepath = input_filepath

    @abstractmethod
    def read_internal(self):
        pass

    @abstractmethod
    def print_raw_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    def read_data(self):
        Logger.log_command(f'reading data')
        self.read_internal()
