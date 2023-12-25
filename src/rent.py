from SalaryCalculations.salary_utils import SalaryUtils


# mySalary = Salary(salary=155_000, roth_deductions=22_500)
# print(f"Semi-monthy:  {format(mySalary.semi_monthy())}")
# print(f"Yearly-savings:  {format(mySalary.recommended_yearly_savings())}")
# print(f"Smart amount on rent:  {format(mySalary.recommended_monthly_rent())}")

rent = 3000
targetSalary = SalaryUtils.rent_to_recommended_salary(rent=rent, roth_deductions=16080)
print(f"With a rent of {format(rent)}, you should make:  {format(targetSalary.salary())}")
print(f"which has a semi-monthly paycheck of {format(targetSalary.semi_monthy())}")
print(f"and a yearly savings of {format(targetSalary.recommended_yearly_savings())}")

# x_axis = np.linspace(1000, 10_000, num=5)
# y_axis = [SalaryUtils.rent_to_recommended_salary(rent=x, roth_deductions=16080).salary()
#       for x in x_axis]

# plt.plot(x_axis, y_axis)
# plt.show()