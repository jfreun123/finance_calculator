from SalaryCalculations.salary import Salary

test = Salary(salary="N/A",
              post_tax_semi_monthly=7083*.93,
              roth_deductions=16080,
              monthly_rent_percent=.35,
              monthly_fun_percent=.35)
print(test)



# test = Salary(salary=178_000,post_tax_semi_monthly=4412*.93 ,roth_deductions=16080)
# print(test)