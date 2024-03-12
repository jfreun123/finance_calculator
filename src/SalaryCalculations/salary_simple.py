class SimpleSalary:
    def __init__(self, yearly_bonus, post_tax_semi_monthly, monthly_rent_percent, monthly_fun_percent, monthly_fun_max=3500):
        self.__monthly_rent_percent = monthly_rent_percent
        self.__monthly_fun_percent = monthly_fun_percent
        self.__monthly_fun_max = monthly_fun_max
        self.__yearly_bonus = yearly_bonus
        self.__post_tax_semi_monthly = post_tax_semi_monthly
    
    def yearly_bonus(self):
        return self.__yearly_bonus
    
    def post_tax_monthly(self):
        return self.__post_tax_semi_monthly * 2
    
    def monthly_savings_no_bonus(self):
        return self.post_tax_monthly() - self.monthly_fun() - self.monthly_rent()
    
    def __yearly_savings_no_bonus(self):
        return 12 * self.monthly_savings_no_bonus()
    
    def recommended_yearly_savings(self):
        return self.__yearly_savings_no_bonus() + self.yearly_bonus()
    
    def monthly_rent(self):
        return self.post_tax_monthly() * self.__monthly_rent_percent
    
    def monthly_fun(self):
        return min(self.post_tax_monthly() * self.__monthly_fun_percent, self.__monthly_fun_max)
    
    def __str__(self):
        res = f"With a semi-monthly paycheck of {format(self.__post_tax_semi_monthly)}\n"
        res += f"and a bonus of {format(self.yearly_bonus())} per year\n"
        res += f"you can save {format(self.recommended_yearly_savings())} per year\n"
        res += f"spend {format(self.monthly_fun())} for fun per month\n"
        res += f"and spend {format(self.monthly_rent())} on rent.\n"
        return res
    



    
    

def format(num):
    return '${:,.2f}'.format(num)