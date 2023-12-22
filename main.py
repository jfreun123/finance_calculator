from plotter import Plotter

from random_walk_simulation import Simulation


sim = Simulation()
plotter = Plotter(starting_age = 23)
points = sim.single_simulation(total_years=10, starting_amount=0)
plotter.basic_plot(points=points)

plotter.plot_all(sim.many_simulations(total_years=10, 
                                      starting_amount=0,
                                      number_of_simulations=10))