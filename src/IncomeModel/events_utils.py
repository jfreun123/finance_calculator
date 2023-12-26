import random

from SalaryCalculations.salary import Salary, format


class Events:
    def __init__(self, retirement_age, inflation, curr_age):
        self.__inflation = inflation
        self.__retirement_age = retirement_age
        self.__age = curr_age
    
    def year_adjusted(self, year):
        return self.__age+year
    
    def random_big_event(self, year):
        n = random.random()
        ret = 0
        if n < .8:
            ret = 0
        elif n < .9:
            ret = -10_000
        elif n < .95:
            ret = -20_000
        else:
            ret = -40_000

        return ret * (self.__inflation ** year)
    
    def random_rate(self, year):
        if (self.year_adjusted(year) >= self.__retirement_age): # if I retire, be safe
            return 1.05

        n = random.random()
        if n <= .2: return 1.15
        elif n <= .8: return 1.07
        return .75
    
    def retire(self, year, curr_amount):
        ret = -50_000 * (self.__inflation ** year)
        return ret
    
    def savings_at_year(self, year, curr_amount):
        if (curr_amount <= 0):
            return 0
        salary = 0            
        if self.year_adjusted(year) <= 24: 
            salary=178_000
        elif self.year_adjusted(year) <= 27: 
            salary=300_000
        elif self.year_adjusted(year) <= 40: 
            salary=700_000
        elif self.year_adjusted(year) < self.__retirement_age: 
            salary=90_000
        else:
            return self.retire(year, curr_amount)
        
    


        sal_obj = Salary(salary=salary, roth_deductions=16_750)
        return (sal_obj.recommended_yearly_savings()
                 * (self.__inflation ** year))
    
    def print_info(self, rate, savings, event, starting_amount, year):
        if (self.year_adjusted(year) == self.__age):
            print("\n%-3s    %-20s   %-4s   %-19s   %-21s   %-19s   %-20s" %
                  ("Age", "Current Balance", 
                   "ROI", "Market Gain", "Salary Savings", 
                   "Random Event", "Net Gain"))
            
        savings_from_investments = (rate - 1) * starting_amount
        net = savings + savings_from_investments + event
        print("%-3.0f    %-20s   %-3.2f   %-20s  %-20s    %-20s  %-20s" % 
              (self.year_adjusted(year), format(starting_amount), rate, 
               format(savings_from_investments), format(savings), 
               format(event), format(net)))
    
    def process_year(self, year, starting_amount):
        
        rate = self.random_rate(year)
        savings = self.savings_at_year(year, curr_amount=starting_amount)
        event = self.random_big_event(year)
        self.print_info(rate=rate, 
                   savings=savings, 
                   event=event, 
                   starting_amount=starting_amount,
                   year=year)
        return (starting_amount * rate) + savings + event