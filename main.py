from pandas_data_collector import PandasDataCollector


def main():
    data_collector = PandasDataCollector('archive/HR-Employee-Attrition.csv')
    data_collector.read_data()
    data_collector.print_raw_data()


if __name__ == '__main__':
    main()
