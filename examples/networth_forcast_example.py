from FinanceTools.IncomeModel.events_utils import Events
from FinanceTools.IncomeModel.random_walk_simulation import Simulation
from FinanceTools.IncomeModel.plotter import Plotter

from FinanceTools.SalaryCalculations.salary_simple import SimpleSalary, InflationAdjustedSalary

import random


curr_age=25
end_age=30

starting_amount=180_000 
yearly_inflation_rate=.03
monthly_rent_percent=.3
monthly_fun_percent=.4

n = 1000

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

    
def savings_at_year(iter) -> InflationAdjustedSalary: 
    simple_sal = SimpleSalary(post_tax_post_roth_base_only_monthly_income=3950*2,
                    monthly_rent=2293,
                    monthly_expense=3000,
                    post_tax_yearly_bonus=.5*31_000,
                    yearly_roth=22_500)
    return InflationAdjustedSalary(simple_salary=simple_sal, inflation_rate=yearly_inflation_rate)

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