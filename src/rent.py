from SalaryCalculations.salary_utils import SalaryUtils

rent = 2400
targetSalary = SalaryUtils.rent_to_recommended_salary(rent=rent, 
                                                      roth_deductions=16080, 
                                                      monthly_rent_percent=.4,
                                                      monthly_fun_percent=.4,
                                                      enable_tax_calculations=False)
print(targetSalary)
