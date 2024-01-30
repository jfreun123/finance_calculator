import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, starting_age=0):
        self.__starting_age = starting_age

    

    def prettify_graph(self, plot, title="Results"):
        fig, ax = plot.subplots(1, 1)

        plot.title(title)
        plot.xlabel("Age")
        plot.ylabel("Net Worth")

        fmt = '${x:,.0f}'
        tick = mtick.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(
            tick) 
        plot.xticks(rotation=25)

    def basic_plot(self, points):
        self.prettify_graph(plot=plt, title="One Result")
        plt.plot(self.__get_x_axis(len(points)), points)
        plt.show()
    
    def plot_all(self, points_gen, number_of_simulations):
        self.prettify_graph(plot=plt, title=f"{number_of_simulations} simulations")
        success_count = 0
        for points, success in points_gen:
            success_count+=(success)
            plt.plot(self.__get_x_axis(len(points)), points)
        print(f"Probability of success:  {success_count/number_of_simulations}")
        plt.show()

    def __get_x_axis(self, size_of_data):
        return range(self.__starting_age, size_of_data + self.__starting_age)
