from IncomeModel.plotter import Plotter

from IncomeModel.random_walk_simulation import Simulation


sim = Simulation(end_age=105, 
                 curr_age=23,
                 retirement_age=60, 
                 starting_amount=30_000, 
                 inflation=1.03)
plotter = Plotter(starting_age = 23)

n = 10
plotter.plot_all(sim.many_simulations(number_of_simulations=n), number_of_simulations=n)