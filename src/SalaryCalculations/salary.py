from tax import Tax


class Salary:
    def __init__(self, salary, roth_deductions, format=True):
        self.__salary = salary
        self.__take_home_salary = self.__calculate_take_home(salary, roth_deductions)
        self.__roth_deductions = roth_deductions
        self.__format = format
    
    def __calculate_take_home(self, salary, roth_deductions):
        salary -= roth_deductions
        ret = salary - Tax.all_tax(salary=salary)
        
        if (self.__format): self.format(ret)
        return ret
    
    def take_home_salary(self):
        return self.__take_home_salary
    
    def roth_deductions(self):
        return self.__roth_deductions
    
    def monthy(self):
        return self.__take_home_salary / 12
    
    def semi_monthy(self):
        return self.__take_home_salary / 24
    
    def recommended_yearly_savings(self):
        return (self.__take_home_salary * .3) + self.__roth_deductions
    
    def format(self, num):
        return '${:,.2f}'.format(num)