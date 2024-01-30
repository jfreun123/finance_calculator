from SalaryCalculations.salary_utils import SalaryUtils

rent = 4500
targetSalary = SalaryUtils.rent_to_recommended_salary(rent=rent, 
                                                      roth_deductions=16080, 
                                                      monthly_rent_percent=.35,
                                                      monthly_fun_percent=.4,
                                                      enable_tax_calculations=True)
print(targetSalary)
