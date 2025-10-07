import random

from FinanceTools.IncomeModel.events_utils import Events
from FinanceTools.IncomeModel.random_walk_simulation import Simulation
from FinanceTools.IncomeModel.plotter import Plotter

from FinanceTools.SalaryCalculations.salary_simple import (
    SimpleSalary,
    InflationAdjustedSalary,
)


CURR_AGE = 25
END_AGE = 50

STARTING_AMOUNT = 185_000
YEARLY_INFLATION_RATE = 0.03

NUMBER_OF_SIMULATIONS = 10_000


def random_big_event(iteration, current_amount):  # pylint: disable=unused-argument
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
    return Events.inflation_adjusted(ret, 1 + YEARLY_INFLATION_RATE, iteration)


def random_rate(iteration):  # pylint: disable=unused-argument
    n = random.random()
    if n <= 0.7:
        return 1.1
    elif n <= 0.9:
        return 1.12
    elif n <= 0.99:
        return 1.15
    return 0.70


def savings_at_year(
    iteration,
) -> InflationAdjustedSalary:  # pylint: disable=unused-argument
    simple_sal = SimpleSalary(
        post_tax_post_roth_base_only_monthly_income=5900 * 2,
        monthly_rent=3500,
        monthly_expense=4000,
        post_tax_yearly_bonus=0.5 * 75_000,
        yearly_roth=22_500,
    )
    return InflationAdjustedSalary(
        simple_salary=simple_sal, inflation_rate=YEARLY_INFLATION_RATE
    )


sim = Simulation(
    starting_amount=STARTING_AMOUNT,
    curr_age=CURR_AGE,
    end_age=END_AGE,
    savings_at_year=savings_at_year,
    random_rate=random_rate,
    random_big_event=random_big_event,
    print_events=True,
)

plotter = Plotter(sim=sim)

plotter.plot_all(number_of_simulations=NUMBER_OF_SIMULATIONS)
