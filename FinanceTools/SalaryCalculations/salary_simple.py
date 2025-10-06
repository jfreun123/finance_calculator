# post_tax_post_roth_base_only_monthly_income does NOT include bonus or roth 
class SimpleSalary:
    def __init__(self, post_tax_post_roth_base_only_monthly_income, monthly_rent, monthly_expense, post_tax_yearly_bonus, yearly_roth):
        self.__post_tax_post_roth_base_only_monthly_income = post_tax_post_roth_base_only_monthly_income
        self.__monthly_rent = monthly_rent
        self.__monthly_expense = monthly_expense
        self.__post_tax_yearly_bonus = post_tax_yearly_bonus
        self.__yearly_roth = yearly_roth

    # Yearly bonus
    def yearly_bonus(self):
        return self.__post_tax_yearly_bonus

    # Roth savings
    def roth_savings(self):
        return self.__yearly_roth

    # Recommended yearly savings = total income - expenses - rent
    def recommended_yearly_savings(self):
        return self.monthly_savings_no_bonus() * 12 + self.__post_tax_yearly_bonus + self.__yearly_roth

    # Monthly savings without bonus
    def monthly_savings_no_bonus(self):
        monthly_savings = self.__post_tax_post_roth_base_only_monthly_income - (self.__monthly_rent + self.__monthly_expense)
        return monthly_savings

    # Monthly fun money
    def monthly_fun(self):
        return self.__monthly_expense

    # Monthly rent
    def monthly_rent(self):
        return self.__monthly_rent

    def __str__(self):
        res = "--------- Stats --------- \n"
        res += f"With a post-tax, post-roth, monthly paycheck of ${self.__post_tax_post_roth_base_only_monthly_income:,.2f}\n"
        res += f"and a post-tax bonus of ${self.yearly_bonus():,.2f} per year\n"
        res += f"and a roth savings of ${self.roth_savings():,.2f} per year\n"
        res += "--------- Yearly --------- \n"
        res += f"you can save ${self.recommended_yearly_savings():,.2f} per year\n"
        res += "--------- Monthly --------- \n"
        res += f"you can save ${self.monthly_savings_no_bonus():,.2f} per month\n"
        res += f"spend ${self.monthly_fun():,.2f} for fun per month\n"
        res += f"and spend ${self.monthly_rent():,.2f} on rent.\n"
        return res