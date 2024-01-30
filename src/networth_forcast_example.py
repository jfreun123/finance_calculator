from IncomeModel.plotter import Plotter
from IncomeModel.events_utils import Events
from IncomeModel.random_walk_simulation import Simulation
from SalaryCalculations.salary import Salary

import random

curr_age=23
end_age=30 
retirement_age=40 
starting_amount=30_000 
yearly_inflation_rate=1.03
roth_deductions=16_750
monthly_rent_percent=.35
monthly_fun_percent=.35
monthly_fun_max=3_500

n = 10

def random_big_event(iter, curr_amount):
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
        return Events.inflation_adjusted(ret, yearly_inflation_rate, iter)

def random_rate(iter):
        if (Events.real_age(iter, curr_age) >= retirement_age): # if I retire, be safe
            return 1.05

        n = random.random()
        if n <= .7: return 1.07
        elif n <= .9: return 1.12
        elif n <= .95: return 1.3
        return .75

    
def savings_at_year(iter, curr_amount):
    def retire(iter, curr_amount):
        if curr_amount==0:
            return 0
        ideal = Events.inflation_adjusted(-50_000, yearly_inflation_rate, iter)
        return ideal
    
    salary = 0    
    age = Events.real_age(iter, curr_age)      
    if age <= 25: 
        salary=190_000
    elif age <= 28: 
        salary=500_000
    elif age <= retirement_age:
        salary=800_000
    else:
        return retire(iter, curr_amount)
    
    sal_obj = Salary(salary=salary, 
                     roth_deductions=roth_deductions, 
                     monthly_rent_percent=monthly_rent_percent, 
                     monthly_fun_percent=monthly_fun_percent,
                     monthly_fun_max=monthly_fun_max)
    return Events.inflation_adjusted(sal_obj.recommended_yearly_savings(), yearly_inflation_rate, iter)

sim = Simulation(starting_amount=starting_amount,
                 curr_age=curr_age,
                 end_age=end_age,
                 savings_at_year=savings_at_year,
                 random_rate=random_rate,
                 random_big_event=random_big_event)
plotter = Plotter(starting_age = curr_age)

plotter.plot_all(sim.many_simulations(number_of_simulations=n), number_of_simulations=n)