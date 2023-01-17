import numpy as np


class AverageStatistics():

    def __init__(self, average_statistics, data):
        self.__average_statistics = average_statistics
        self.__statistics_data_frame = data

    def get_main_criteria(self):
        return self.__main_criteria

    def set_main_criteria(self, main_criteria):
        self.__main_criteria = main_criteria

    def print_statistics_summary(self, precision=0):
        print('Average statistics:')

        for attribute, value in self.__average_statistics.items():
            print(f'Average {attribute}: {value:.{precision}f}')

    def get_statistics(self, attribute, ascending=True):
        grouped_statistics = self.__statistics_data_frame[[
            self.__main_criteria, attribute]].groupby([self.__main_criteria])
        return grouped_statistics.mean().sort_values(by=self.__main_criteria, ascending=ascending)

    def print_statistics_data(self, sort_by, ascending=False):
        grouped_statistics = self.__statistics_data_frame.groupby(
            [self.__main_criteria]).mean().sort_values(by=sort_by, ascending=ascending)

        print(f'Average statistics by: {sort_by}')
        print(grouped_statistics)
