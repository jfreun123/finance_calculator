
import pytest
from FinanceTools.SalaryCalculations.salary_simple import SimpleSalary, InflationAdjustedSalary


bloomberg = SimpleSalary(post_tax_post_roth_base_only_monthly_income=3950*2,
                    monthly_rent=2293,
                    monthly_expense=3000,
                    post_tax_yearly_bonus=.5*31_000,
                    yearly_roth=22_500)

def test_bloomberg():
    assert bloomberg.yearly_bonus() == 15500
    assert bloomberg.roth_savings() == 22500
    assert bloomberg.recommended_yearly_savings() == 15500 + 22500 + (3950*2 - (2293 + 3000))*12
    assert bloomberg.monthly_savings_no_bonus() == (3950*2 - (2293 + 3000))
    assert bloomberg.monthly_fun() == 3000
    assert bloomberg.monthly_rent() == 2293

def test_inflation_bloomberg():
    inflation_bloomberg  = InflationAdjustedSalary(simple_salary=bloomberg, inflation_rate=0.03)
    assert inflation_bloomberg.yearly_bonus() == 15500
    assert inflation_bloomberg.yearly_bonus(years=10) == 15500 * (1.03 ** 10)

    assert inflation_bloomberg.roth_savings() == 22500

    curr_expected_savings = 15500 + 22500 + (3950*2 - (2293 + 3000))*12  
    assert inflation_bloomberg.recommended_yearly_savings() == curr_expected_savings     
    assert inflation_bloomberg.recommended_yearly_savings(years=10) == curr_expected_savings * (1.03 ** 10)

    assert inflation_bloomberg.monthly_fun() == 3000
    assert inflation_bloomberg.monthly_fun(years=10) == 3000 * (1.03 ** 10)

    assert inflation_bloomberg.monthly_rent() == 2293
    assert inflation_bloomberg.monthly_rent(years=10) == 2293 * (1.03 ** 10)


