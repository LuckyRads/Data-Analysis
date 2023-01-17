import pandas

from analyzer import Analyzer
from logger import Logger


class HrAnalyzer(Analyzer):

    def __convert_to_attributions(self):
        pass
        # self.__hr_attributions = []
        # for entry in transformed_data.s:
        #     for value in entry:
        #         hr_attribution.append(value)
        #     self.__hr_attributions.append(hr_attribution)

    def transform_dataset(self):
        # self._data = self._data.drop(
        #     ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours', 'YearsWithCurrManager', 'YearsSinceLastPromotion', 'YearsAtCompany', 'WorkLifeBalance', 'TrainingTimesLastYear'], axis=1)
        self.__transformed_data = self._data[['Age', 'Attrition', 'BusinessTravel', 'DailyRate',
                                              'Department', 'DistanceFromHome', 'Education', 'EducationField']]
        self.__convert_to_attributions()

    def print_raw_data(self):
        print(self._data)

    def print_statistics(self, statistic_type, attributes=['Age']):
        for attribute in attributes:
            if statistic_type == 'average':
                Logger.log_result(
                    f'Average {attribute}: {self.__transformed_data[attribute].mean()}')

    def get_average_employee_age(self):
        return self.__transformed_data['Age'].mean()
