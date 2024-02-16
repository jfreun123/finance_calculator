from SalaryCalculations.salary import Salary
real = 3_531.74
sa_pred = 3_810
r = real / sa_pred
test = Salary(salary="N/A",
              post_tax_semi_monthly=5044 * r,
              roth_deductions=16080,
              monthly_rent_percent=.4,
              monthly_fun_percent=.4)
print(test)



# test = Salary(salary=178_000,post_tax_semi_monthly=4412*.93 ,roth_deductions=16080)
# print(test)