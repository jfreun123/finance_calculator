import random

from SalaryCalculations.salary import Salary


class Events:
    def __init__(self, retirement_year, inflation):
        self.__inflation = inflation
        self.__retirement_year = retirement_year

    def random_big_event(self, year):
        n = random.random()
        ret = 0
        if n < .5:
            ret = 0
        elif n < .75:
            ret = 10_000
        elif n < .95:
            ret = 20_000
        else:
            ret = 40_000
        return ret * (self.__inflation ** year)
    
    def random_rate(self, year):
        if (year >= self.__retirement_year): # if I retire, be safe
            return 1.05
        n = random.random()
        if n <= .2: return 1.15
        elif n <= .8: return 1.07
        return .75
    
    def retire(self, year, curr_amount):
        ret = -curr_amount * .04
        print(f"Lost {ret} at year {year}")
        return ret
    
    def savings_at_year(self, year, curr_amount=0):
        salary = 0
        if (year + 23) <= 24: 
            salary=178_000
        elif (year + 23) <= 27: 
            salary=300_000
        elif (year + 23) <= 30: 
            salary=400_000
        elif (year + 23) <= self.__retirement_year: 
            salary=700_000
        else:
            return self.retire(year, curr_amount)

        sal_obj = Salary(salary=salary, roth_deductions=16_750)
        # print(f"Year:  {year}")
        # print(sal_obj)
        return (sal_obj.recommended_yearly_savings()
                 * (self.__inflation ** year))
    
    def process_year(self, year, starting_amount):
        starting_amount *= self.random_rate(year)
        starting_amount += self.savings_at_year(year, curr_amount=starting_amount)
        starting_amount -= self.random_big_event(year)
        return starting_amount