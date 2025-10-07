# post_tax_post_roth_base_only_monthly_income does NOT include bonus or roth
class SimpleSalary:
    def __init__(
        self,
        post_tax_post_roth_base_only_monthly_income,
        monthly_rent,
        monthly_expense,
        post_tax_yearly_bonus,
        yearly_roth,
    ):
        self.__post_tax_post_roth_base_only_monthly_income = (
            post_tax_post_roth_base_only_monthly_income
        )
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
        return (
            self.monthly_savings_no_bonus() * 12
            + self.__post_tax_yearly_bonus
            + self.__yearly_roth
        )

    # Monthly savings without bonus
    def monthly_savings_no_bonus(self):
        monthly_savings = self.__post_tax_post_roth_base_only_monthly_income - (
            self.__monthly_rent + self.__monthly_expense
        )
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


class InflationAdjustedSalary:
    """
    Wraps a SimpleSalary instance and provides inflation-adjusted projections.
    """

    def __init__(self, simple_salary: SimpleSalary, inflation_rate=0.03):
        self.salary = simple_salary
        self.inflation_rate = inflation_rate

    def adjust_for_inflation(self, amount, years):
        """Calculate future value after inflation for a given number of years."""
        return amount * ((1 + self.inflation_rate) ** years)

    # Inflation-adjusted versions of SimpleSalary methods
    def recommended_yearly_savings(self, years=0):
        base = self.salary.recommended_yearly_savings()
        return self.adjust_for_inflation(base, years) if years > 0 else base

    def monthly_savings_no_bonus(self, years=0):
        base = self.salary.monthly_savings_no_bonus()
        return self.adjust_for_inflation(base, years) if years > 0 else base

    def monthly_fun(self, years=0):
        base = self.salary.monthly_fun()
        return self.adjust_for_inflation(base, years) if years > 0 else base

    def monthly_rent(self, years=0):
        base = self.salary.monthly_rent()
        return self.adjust_for_inflation(base, years) if years > 0 else base

    def yearly_bonus(self, years=0):
        base = self.salary.yearly_bonus()
        return self.adjust_for_inflation(base, years) if years > 0 else base

    def roth_savings(self, years=0):
        base = self.salary.roth_savings()
        return self.adjust_for_inflation(base, years) if years > 0 else base

    # String representation including optional inflation adjustment
    def __str__(self, projection_years=5):
        res = "--------- Current Stats --------- \n"
        res += str(self.salary) + "\n"
        if projection_years > 0:
            res += f"--------- Inflation Adjusted Projection ({projection_years} years at {self.inflation_rate*100:.1f}%/year) ---------\n"
            res += f"Savings in {projection_years} years: ${self.recommended_yearly_savings(projection_years):,.2f}\n"
            res += f"Monthly savings in {projection_years} years: ${self.monthly_savings_no_bonus(projection_years):,.2f}\n"
            res += f"Fun money in {projection_years} years: ${self.monthly_fun(projection_years):,.2f}\n"
            res += f"Rent in {projection_years} years: ${self.monthly_rent(projection_years):,.2f}\n"
            res += f"Bonus in {projection_years} years: ${self.yearly_bonus(projection_years):,.2f}\n"
            res += f"Roth in {projection_years} years: ${self.roth_savings(projection_years):,.2f}\n"
        return res
