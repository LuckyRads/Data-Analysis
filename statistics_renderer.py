import matplotlib.pyplot as plt
import numpy as np


class StatisticsRenderer():

    def draw_bar_plot(self, x_label, y_label, title, x_values, y_values):
        plt.plot(x_values, y_values)

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.show()
