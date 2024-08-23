from FinanceTools.SalaryCalculations.tax import Tax


class Salary:
    __ROTH_MAX = 22_500

    def __init__(self, roth_deductions, salary, monthly_rent_percent, monthly_fun_percent, monthly_fun_max=3500, post_tax_semi_monthly="N/A"):
        self.__roth_deductions = roth_deductions
        self.__salary = salary
        self.__monthly_rent_percent = monthly_rent_percent
        self.__monthly_fun_percent = monthly_fun_percent
        self.__monthly_fun_max = monthly_fun_max
        self.__take_home_salary = self.__calculate_take_home(salary, roth_deductions, post_tax_semi_monthly)
        

    

    
    def __calculate_take_home(self, salary, roth_deductions, post_tax_semi_monthly):
        if (post_tax_semi_monthly == "N/A"):
            return max(salary - Tax.all_tax(salary=salary) - roth_deductions, 0)
        else:
            return 24 * post_tax_semi_monthly
        
    def salary(self):
        return self.__salary
    
    def take_home_salary(self):
        return self.__take_home_salary
    
    def roth_deductions(self):
        return self.__roth_deductions
    
    def monthly(self):
        return self.__take_home_salary / 12
    
    def semi_monthly(self):
        return self.__take_home_salary / 24
    
    def recommended_yearly_savings(self):
        return (12 *(self.monthly() - self.monthly_fun() - self.monthly_rent())) + Salary.__ROTH_MAX
    
    def monthly_rent(self):
        return self.monthly() * self.__monthly_rent_percent
    
    def monthly_fun(self):
        return min(self.monthly() * self.__monthly_fun_percent, self.__monthly_fun_max)
    
    def __str__(self):
        res = f"\nWith a salary of {format(self.salary()) if type(self.salary()) == int else self.salary()} and roth deductions of {format(self.roth_deductions())}\n"
        res += f"you will have a semi-monthly paycheck of {format(self.semi_monthly())} and\n"
        res += f"you can save {format(self.recommended_yearly_savings())} per year\n"
        res += f"spend {format(self.monthly_fun())} for fun per month\n"
        res += f"and spend {format(self.monthly_rent())} on rent.\n"
        return res
    



    
    

def format(num):
    return '${:,.0f}'.format(num)