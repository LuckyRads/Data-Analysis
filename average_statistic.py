class AverageStatistics():

    def __init__(self, raw_statistics):
        self.__age = raw_statistics['Age']
        self.__daily_rate = raw_statistics['DailyRate']
        self.__distance_from_home = raw_statistics['DistanceFromHome']

    def print_statistics(self, precision=0):
        print(f'Average age: {round(self.__age, precision)}')
        print(f'Average daily rate: {round(self.__daily_rate, precision)}')
        print(
            f'Average distance from home: {round(self.__distance_from_home, precision)}')
