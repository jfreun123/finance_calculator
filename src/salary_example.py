from SalaryCalculations.salary_simple import SimpleSalary
real = 3_531.74
sa_pred = 3_579
r = real / sa_pred
test = SimpleSalary(post_tax_semi_monthly=5911*r,
                    yearly_bonus=160_000*.6+22_500,
                    monthly_rent_percent=.5,
                    monthly_fun_percent=.4)
print(test)



# test = Salary(salary=178_000,post_tax_semi_monthly=4412*.93 ,roth_deductions=16080)
# print(test)