import pandas

from analyzer import Analyzer
from logger import Logger


class HrAnalyzer(Analyzer):

    def __does_attribute_fit_statistic_type(self, attribute: str, statistic_type: str) -> bool:
        if statistic_type.lower() == 'average':
            return self.__transformed_data[attribute].dtype in ['int64', 'float64']
        return False

    def transform_dataset(self):
        self.__transformed_data = self._data[['Age', 'Attrition', 'BusinessTravel', 'DailyRate',
                                              'Department', 'DistanceFromHome', 'Education', 'EducationField']]
        self.__convert_to_attributions()

    def print_raw_data(self):
        print(self._data)

    def print_statistics(self, statistic_type, attributes, precision=2):
        for attribute in attributes:
            if not self.__does_attribute_fit_statistic_type(attribute, statistic_type):
                Logger.log_error(
                    f'Attribute {attribute} does not fit statistic type {statistic_type}')
                continue

            if statistic_type.lower() == 'average':
                raw_statistic = self.__transformed_data[attribute].mean()

            rounded_statistic = round(raw_statistic, precision)
            Logger.log_result(
                f'{statistic_type}: {attribute}: {rounded_statistic}')
