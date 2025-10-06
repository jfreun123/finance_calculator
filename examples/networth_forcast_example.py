from FinanceTools.IncomeModel.events_utils import Events
from FinanceTools.IncomeModel.random_walk_simulation import Simulation
from FinanceTools.IncomeModel.plotter import Plotter

from FinanceTools.SalaryCalculations.salary_simple import SimpleSalary

import random


curr_age=25
end_age=30

starting_amount=180_000 
yearly_inflation_rate=1.03
monthly_rent_percent=.4
monthly_fun_percent=.3

n = 100

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
        n = random.random()
        if n <= .7: return 1.11
        elif n <= .9: return 1.15
        elif n <= .99: return 1.3
        return .75

    
def savings_at_year(iter, curr_amount):
    post_tax_semi_monthly=5950 # 163k
    yearly_bonus = 75_000

    
    sal_obj = SimpleSalary(post_tax_semi_monthly=post_tax_semi_monthly,
                           monthly_rent_percent=monthly_rent_percent,
                           monthly_fun_percent=monthly_fun_percent,
                           post_tax_yearly_bonus=22_500+(yearly_bonus*.5))
    return Events.inflation_adjusted(sal_obj.recommended_yearly_savings(), yearly_inflation_rate, iter)

sim = Simulation(starting_amount=starting_amount,
                 curr_age=curr_age,
                 end_age=end_age,
                 savings_at_year=savings_at_year,
                 random_rate=random_rate,
                 random_big_event=random_big_event,
                 print_events=True
                 )

plotter = Plotter(sim=sim)

plotter.plot_all(number_of_simulations=n)