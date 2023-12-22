import matplotlib.pyplot as plt
class Plotter:
    def __init__(self, starting_age=0):
        self.__starting_age = starting_age
    def basic_plot(self, points):
        plt.plot(self.__get_x_axis(len(points)), points)
        plt.show()
    
    def plot_all(self, points_gen):
        for points in points_gen:
            plt.plot(self.__get_x_axis(len(points)), points)
        plt.show()

    def __get_x_axis(self, size_of_data):
        return range(self.__starting_age, size_of_data + self.__starting_age)
