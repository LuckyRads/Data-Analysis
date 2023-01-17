import matplotlib.pyplot as plt
import numpy as np


class StatisticsRenderer():

    def __init__(self, color, line_width):
        self.__color = color
        self.__line_width = line_width

    def draw_plot(self, x_label, y_label, title, data_frame):
        x_values = data_frame.index.values
        y_values = data_frame.values

        plt.plot(x_values, y_values, color=self.__color,
                 linewidth=self.__line_width)

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.show()
