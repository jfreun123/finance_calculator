import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, sim, setting="DEFAULT"):
        self.__sim = sim
        self.__starting_age = sim.get_starting_age()
        self.__setting  = setting
        self.__age_axis = range(self.__starting_age, sim.get_total_iters() + self.__starting_age+1)

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

    def plot_all(self, number_of_simulations):
        if (self.__setting == "DL_REGRESSION"):
            y_points, y_pred = self.__sim.deep_learning_linear_regression(number_of_simulations)
            self.plot_all_dl(y_points,y_pred, number_of_simulations)
        elif (self.__setting == "DL_FULL"):
            y_points, y_pred = self.__sim.deep_learning_full(number_of_simulations)
            self.plot_all_dl(y_points,y_pred, number_of_simulations)
        else:
            self.plot_all_no_dl(self.__sim.many_simulations(number_of_simulations),
                            number_of_simulations)

    def plot_all_no_dl(self, points_gen, number_of_simulations):
        self.prettify_graph(plot=plt, title=f"{number_of_simulations} simulations")
        success_count = 0
        for sample, success in points_gen:
            success_count+=(success)
            plt.plot(self.__age_axis, sample)
        print(f"Probability of success:  {success_count/number_of_simulations}")
        plt.show()
    
    def plot_all_dl(self, y_points, y_pred, number_of_simulations):
        self.prettify_graph(plot=plt, title=f"{number_of_simulations} simulations")
        size_of_data = len(y_points[0])
        for sample in y_points:
            plt.scatter(self.__age_axis, sample)
        plt.plot(self.__get_x_axis(size_of_data), y_pred.data.cpu().numpy(), 'r-', lw=5)
        plt.show()
