from IncomeModel.plotter import Plotter
from IncomeModel.events_utils import Events
from IncomeModel.random_walk_simulation import Simulation
from SalaryCalculations.salary import Salary

import random

end_age=105 
curr_age=23
retirement_age=40 
starting_amount=30_000 
inflation=1.03
roth_deductions=16_750
monthly_rent_percent=.1
monthly_fun_percent=.1

n = 10

def random_big_event(year, curr_amount):
        if (curr_amount == 0):
            return 0
        n = random.random()
        ret = 0
        if n < .8:
            ret = 0
        elif n < .9:
            ret = -10_000
        elif n < .95:
            ret = -20_000
        else:
            ret = -40_000
        return ret * (inflation ** year)

def random_rate(year):
        if (Events.year_adjusted(year, curr_age) >= retirement_age): # if I retire, be safe
            return 1.05

        n = random.random()
        if n <= .7: return 1.07
        elif n <= .8: return 1.20
        return .75

    
def savings_at_year(year, curr_amount):
    def retire( year, curr_amount):
            ideal = -50_000 * (inflation ** year)
            return ideal
    if (curr_amount <= 0):
        return 0
    
    salary = 0            
    if Events.year_adjusted(year, curr_age) <= 25: 
        salary=190_000
    elif Events.year_adjusted(year, curr_age) <= 28: 
        salary=300_000
    elif Events.year_adjusted(year, curr_age) <= retirement_age:
        salary=600_000
    else:
        return retire(year, curr_amount)
    
    sal_obj = Salary(salary=salary, roth_deductions=roth_deductions, monthly_rent_percent=monthly_rent_percent, monthly_fun_percent=monthly_fun_percent)
    return (sal_obj.recommended_yearly_savings()
                * (inflation ** year))

sim = Simulation(starting_amount=starting_amount,
                 curr_age=curr_age,
                 end_age=end_age,
                 savings_at_year=savings_at_year,
                 random_rate=random_rate,
                 random_big_event=random_big_event)
plotter = Plotter(starting_age = curr_age)

plotter.plot_all(sim.many_simulations(number_of_simulations=n), number_of_simulations=n)