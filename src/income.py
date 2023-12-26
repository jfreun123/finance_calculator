from IncomeModel.plotter import Plotter

from IncomeModel.random_walk_simulation import Simulation


sim = Simulation(end_age=105, 
                 curr_age=23,
                 retirement_age=70, 
                 starting_amount=30_000, 
                 inflation=1.03)
plotter = Plotter(starting_age = 23)
# points = sim.single_simulation()
# plotter.basic_plot(points=points)

n = 1
plotter.plot_all(sim.many_simulations(number_of_simulations=n), number_of_simulations=n)