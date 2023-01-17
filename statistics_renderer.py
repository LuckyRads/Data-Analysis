import matplotlib.pyplot as plt
import numpy as np


class StatisticsRenderer():

    def draw_bar_plot(self, dict_of_statistics, x_label, y_label, title):
        x_array = np.array(list(dict_of_statistics.keys()))
        y_array = np.array(list(dict_of_statistics.values()))

        figure = plt.figure()
        ax = figure.add_axes([0, 0, 1, 1])

        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        ax.bar(x_array, y_array)

        plt.show()
