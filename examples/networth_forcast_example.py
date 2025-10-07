from FinanceTools.IncomeModel.events_utils import Events
from FinanceTools.IncomeModel.random_walk_simulation import Simulation
from FinanceTools.IncomeModel.plotter import Plotter

from FinanceTools.SalaryCalculations.salary_simple import (
    SimpleSalary,
    InflationAdjustedSalary,
)

import random


curr_age = 24
end_age = 30

starting_amount = 217_000
yearly_inflation_rate = 0.03

n = 1000


def random_big_event(iter, curr_amount):
    n = random.random()
    ret = 0
    if n < 0.8:
        ret = 0
    elif n < 0.9:
        ret = -10_000
    elif n < 0.95:
        ret = -20_000
    else:
        ret = -40_000
    return Events.inflation_adjusted(ret, 1 + yearly_inflation_rate, iter)


def random_rate(iter):
    n = random.random()
    if n <= 0.7:
        return 1.1
    elif n <= 0.9:
        return 1.12
    elif n <= 0.99:
        return 1.15
    return 0.70


def savings_at_year(iter) -> InflationAdjustedSalary:
    simple_sal = SimpleSalary(
        post_tax_post_roth_base_only_monthly_income=2500 * 2,
        monthly_rent=1925,
        monthly_expense=2250,
        post_tax_yearly_bonus=0.5 * 15_000 + 10_000,
        yearly_roth=20_000,
    )
    return InflationAdjustedSalary(
        simple_salary=simple_sal, inflation_rate=yearly_inflation_rate
    )


sim = Simulation(
    starting_amount=starting_amount,
    curr_age=curr_age,
    end_age=end_age,
    savings_at_year=savings_at_year,
    random_rate=random_rate,
    random_big_event=random_big_event,
    print_events=True,
)

plotter = Plotter(sim=sim)

plotter.plot_all(number_of_simulations=n)
