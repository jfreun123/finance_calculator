
import pytest
from FinanceTools.SalaryCalculations.salary_simple import SimpleSalary


def test_bloomberg():
    bloomberg = SimpleSalary(post_tax_post_roth_base_only_monthly_income=3950*2,
                        monthly_rent=2293,
                        monthly_expense=3000,
                        post_tax_yearly_bonus=.5*31_000,
                        yearly_roth=22_500)
    assert bloomberg.yearly_bonus() == 15500
    assert bloomberg.roth_savings() == 22500
    assert bloomberg.recommended_yearly_savings() == 15500 + 22500 + (3950*2 - (2293 + 3000))*12
    assert bloomberg.monthly_savings_no_bonus() == (3950*2 - (2293 + 3000))
    assert bloomberg.monthly_fun() == 3000
    assert bloomberg.monthly_rent() == 2293
    print(bloomberg)
