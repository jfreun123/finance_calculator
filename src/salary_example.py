from SalaryCalculations.salary_simple import SimpleSalary
real = 3_531.74
sa_pred = 3_579
r = real / sa_pred

citadel = SimpleSalary(post_tax_semi_monthly=4562*r,
                    post_tax_yearly_bonus=30_000*.49,
                    roth_savings=22_500,
                    monthly_rent_percent=.4,
                    monthly_fun_percent=.6)
print(citadel)



# test = Salary(salary=178_000,post_tax_semi_monthly=4412*.93 ,roth_deductions=16080)
# print(test)