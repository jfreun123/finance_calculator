from salary import Salary
from tax import Tax



mySalary = Salary(salary=155_000, roth_deductions=22_500)
print(f"Semi-monthy:  {'${:,.2f}'.format(mySalary.semi_monthy())}")
print(f"Yearly-savings:  {mySalary.recommended_yearly_savings()}")

