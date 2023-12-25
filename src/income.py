from IncomeModel.plotter import Plotter

from IncomeModel.random_walk_simulation import Simulation


sim = Simulation(total_years=97-23, 
                 starting_amount=30_000, 
                 retirement_year=40-23, 
                 inflation=1.03)
plotter = Plotter(starting_age = 23)
# points = sim.single_simulation()
# plotter.basic_plot(points=points)

n = 5
plotter.plot_all(sim.many_simulations(number_of_simulations=n), number_of_simulations=n)