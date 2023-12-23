from plotter import Plotter

from random_walk_simulation import Simulation


sim = Simulation(total_years=10, starting_amount=0)
plotter = Plotter(starting_age = 23)
points = sim.single_simulation()
plotter.basic_plot(points=points)

plotter.plot_all(sim.many_simulations(number_of_simulations=10))