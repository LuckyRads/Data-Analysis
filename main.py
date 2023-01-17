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

    attribute_to_analyze_1 = 'Age'
    attribute_to_analyze_2 = 'DailyRate'
    attribute_to_analyze_3 = 'DistanceFromHome'
    attribute_to_analyze_4 = 'YearsAtCompany'

    attributes_to_analyze = [attribute_to_analyze_1, attribute_to_analyze_2,
                             attribute_to_analyze_3, attribute_to_analyze_4]

    # Specific analyzers can retrieve statistics for specific attributes.
    average_statistics = case_analyzer.get_average_statistics(
        attributes_to_analyze)
    average_statistics.print_statistics_summary()

    renderer = StatisticsRenderer()

    # Set base analysis criteria.
    average_statistics.set_main_criteria(attribute_to_analyze_1)

    average_statistics.print_statistics_data(attribute_to_analyze_3)

    age_to_pay_slice = average_statistics.get_statistics(
        attribute_to_analyze_2)
    renderer.draw_plot('Age', 'Average daily rate',
                       'Average daily rate for age', age_to_pay_slice)

    age_to_distance = average_statistics.get_statistics(attribute_to_analyze_3)
    renderer.draw_plot('Age', 'Average distance from home',
                       'Average distance from home for age', age_to_distance)


if __name__ == '__main__':
    main()
