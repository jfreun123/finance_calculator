import matplotlib
matplotlib.use('TkAgg')
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, sim):
        self.__sim = sim
        self.__starting_age = sim.get_starting_age()
        self.__age_axis = range(self.__starting_age, sim.get_total_iters() + self.__starting_age+1)

    def prettify_graph(self, plot, title="Results"):
        _, ax = plot.subplots(1, 1)

        plot.title(title)
        plot.xlabel("Age")
        plot.ylabel("Net Worth")

        fmt = '${x:,.0f}'
        tick = mtick.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(
            tick) 
        plot.xticks(rotation=25)


    def plot_all(self, number_of_simulations):
        points_gen = self.__sim.many_simulations(number_of_simulations)
        self.prettify_graph(plot=plt, title=f"{number_of_simulations} simulations")
        success_count = 0
        for sample, success in points_gen:
            success_count+=(success)
            plt.plot(self.__age_axis, sample)
        print(f"Probability of success:  {success_count/number_of_simulations}")
        plt.show()
