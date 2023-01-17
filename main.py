from hr_analyzer import HrAnalyzer
from pandas_data_collector import PandasDataCollector
from statistics_renderer import StatisticsRenderer


def main():
    # Data collector collects data using pandas data collector implementation.
    data_collector = PandasDataCollector('archive/HR-Employee-Attrition.csv')
    data_collector.read_data()
    data_collector.print_raw_data()

    # Pass a data collector to an analyzer in order for it to load and transform data for further analysis.
    case_analyzer = HrAnalyzer(data_collector)
    case_analyzer.transform_dataset()

    # Specific analyzers can retrieve statistics for specific attributes.
    average_statistics = case_analyzer.get_average_statistics(
        ['Age', 'DailyRate', 'DistanceFromHome'])
    average_statistics.print_statistics()

    average_rates_for_age = case_analyzer.get_average_rates_for('Age')
    average_rates_arrays = HrAnalyzer.transform_statistics_to_arrays(
        average_rates_for_age)

    renderer = StatisticsRenderer()
    renderer.draw_bar_plot('Age', 'Average daily rate', 'Average daily rate for age',
                           average_rates_arrays[0], average_rates_arrays[1])


if __name__ == '__main__':
    main()
