from SalaryCalculations.salary_utils import SalaryUtils

rent = 12_000
targetSalary = SalaryUtils.rent_to_recommended_salary(rent=rent, 
                                                      roth_deductions=16080, 
                                                      monthly_rent_percent=.4,
                                                      monthly_fun_percent=.4,
                                                      enable_tax_calculations=True)
print(targetSalary)
