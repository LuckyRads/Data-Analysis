import numpy as np
import pandas

from analyzer import Analyzer
from average_statistic import AverageStatistics
from logger import Logger


class HrAnalyzer(Analyzer):

    __attributes_to_analyze = ['Age', 'Attrition', 'BusinessTravel', 'DailyRate',
                               'Department', 'DistanceFromHome', 'Education', 'EducationField']

    def get_attributes_to_analyze(self):
        return self.__attributes_to_analyze

    def set_attributes_to_analyze(self, attributes: list):
        self.__attributes_to_analyze = attributes

    def __does_attribute_fit_statistic_type(self, attribute: str, statistic_type: str) -> bool:
        try:
            if statistic_type.lower() == 'average':
                return self.__transformed_data[attribute].dtype in ['int64', 'float64']
        except KeyError:
            Logger.log_error(f'Attribute {attribute} does not exist')
        return False

    def __get_raw_statistic_by_type(self, statistics_type: str, attribute: str):
        try:
            if statistics_type.lower() == 'average':
                return self.__transformed_data[attribute].mean()
            else:
                Logger.log_error(
                    f'Statistic type {statistics_type} is not supported')
            return None
        except KeyError:
            Logger.log_error(f'Attribute {attribute} does not exist')
        return None

    def transform_dataset(self):
        self.__transformed_data = self._data[self.__attributes_to_analyze]

    def print_raw_data(self):
        print(self._data)

    def get_statistics(self, statistics_type, attributes):
        statistics = {}

        for attribute in attributes:
            if not self.__does_attribute_fit_statistic_type(attribute, statistics_type):
                Logger.log_error(
                    f'Attribute {attribute} does not fit statistic type {statistics_type}')
                continue

            raw_statistic = self.__get_raw_statistic_by_type(
                statistics_type, attribute)
            statistics[attribute] = raw_statistic

        return statistics

    def get_average_rates_for(self, attribute='Age', mean=True):
        parameter = 'DailyRate'

        attributes = np.array(self.__transformed_data[attribute])
        rates = np.array(self.__transformed_data[parameter])

        average_rates = {}
        for i in range(len(attributes)):
            if attributes[i] not in average_rates:
                average_rates[attributes[i]] = []
            average_rates[attributes[i]].append(rates[i])

        if mean is True:
            for key, value in average_rates.items():
                average_rates[key] = np.mean(value)
            return average_rates
        else:
            return average_rates

    def get_average_statistics(self, attributes):
        statistics = self.get_statistics('average', attributes)
        return AverageStatistics(statistics)

    def print_statistics(self, statistic_type: str, attributes: str, precision=0):
        statistics = self.get_statistics(statistic_type, attributes)
        for attribute, value in statistics.items():
            Logger.log_result(
                f'{statistic_type.capitalize()} {attribute}: {round(value, precision)}')
