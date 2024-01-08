from SalaryCalculations.salary_utils import SalaryUtils

rent = 3700
targetSalary = SalaryUtils.rent_to_recommended_salary(rent=rent, roth_deductions=16080)
print(targetSalary)
