from SalaryCalculations.tax import Tax


class Salary:
    __ROTH_MAX = 22_500

    def __init__(self, roth_deductions, salary, post_tax_semi_monthly=0):
        self.__salary = salary
        self.__roth_deductions = roth_deductions
        if (post_tax_semi_monthly == 0):
            self.__take_home_salary = self.__calculate_take_home(salary, roth_deductions)
        if(post_tax_semi_monthly != 0):
            self.__take_home_salary = 24 * post_tax_semi_monthly

    

    
    def __calculate_take_home(self, salary, roth_deductions):
        ret = salary - Tax.all_tax(salary=salary) - roth_deductions
        return max(ret, 0)
    
    def salary(self):
        return self.__salary
    
    def take_home_salary(self):
        return self.__take_home_salary
    
    def roth_deductions(self):
        return self.__roth_deductions
    
    def monthy(self):
        return self.__take_home_salary / 12
    
    def semi_monthy(self):
        return self.__take_home_salary / 24
    
    def recommended_yearly_savings(self):
        return (self.__take_home_salary * .3) + Salary.__ROTH_MAX
    
    def recommended_monthly_rent(self):
        return (self.__take_home_salary * .35) / 12
    
    def __str__(self):
        res = f"\nWith a salary of {format(self.salary())} and roth deductions of {format(self.roth_deductions())}\n"
        res += f"you will have a semi-monthly paycheck of {format(self.semi_monthy())} and\n"
        res += f"you can save {format(self.recommended_yearly_savings())} per year\n"
        res += f"and spend {format(self.recommended_monthly_rent())} on rent.\n"
        return res
    
    

def format(num):
    return '${:,.2f}'.format(num)