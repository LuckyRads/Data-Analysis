import numpy as np


class AverageStatistics():

    def __init__(self, average_statistics, data):
        self.__average_statistics = average_statistics
        self.__statistics_data_frame = data

    def set_main_criteria(self, main_criteria):
        self.__main_criteria = main_criteria

    def print_statistics(self, precision=0):
        print('Average statistics:')

        for attribute, value in self.__average_statistics.items():
            print(f'Average {attribute}: {value:.{precision}f}')

    def get_statistics(self, attribute):
        grouped_statistics = self.__statistics_data_frame[[
            self.__main_criteria, attribute]].groupby([self.__main_criteria])
        return grouped_statistics.mean().sort_values(by=self.__main_criteria, ascending=True)
