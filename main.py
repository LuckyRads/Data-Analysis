from hr_analyzer import HrAnalyzer
from pandas_data_collector import PandasDataCollector


def main():
    data_collector = PandasDataCollector('archive/HR-Employee-Attrition.csv')
    data_collector.read_data()
    data_collector.print_raw_data()

    case_analyzer = HrAnalyzer(data_collector.get_data())
    case_analyzer.transform_dataset()
    case_analyzer.print_raw_data()
    case_analyzer.print_statistics('average')


if __name__ == '__main__':
    main()
