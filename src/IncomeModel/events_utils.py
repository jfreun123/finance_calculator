import random


class Events:
    def __init__(self, inflation=1.04):
        self.__inflation = inflation

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
    
    def random_rate(self):
        n = random.random()
        if n <= .1: return 1.15
        if n <= .8: return 1.05
        if n <= 1:  return .75
    
    def savings_at_year(self, year):
        if (year + 23) <= 25: return 25_000 * (self.__inflation ** year)
        if (year + 23) <= 25: return 25_000 * (self.__inflation ** year)
        if (year + 23) <= 25: return 25_000 * (self.__inflation ** year)
        return 
    
    def process_year(self, year, starting_amount):
        starting_amount *= self.random_rate()
        starting_amount += self.savings_at_year(year)
        starting_amount -= self.random_big_event(year)
        return starting_amount