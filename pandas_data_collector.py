import pandas

from data_collector import DataCollector
from logger import Logger


class PandasDataCollector(DataCollector):

    def __init__(self, input_filepath):
        super().__init__(input_filepath)

    def read_internal(self):
        self.__data = pandas.read_csv(self.filepath)

    def get_data(self):
        return self.__data

    def print_raw_data(self):
        Logger.log_result(self.__data)
