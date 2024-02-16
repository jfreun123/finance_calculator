from SalaryCalculations.salary import Salary, format


class Events:
    def __init__(self, curr_age, end_age, random_rate, savings_at_year, random_big_event, print_events=False):
        self.__age = curr_age
        self.__end_age = end_age
        self.__random_rate = random_rate
        self.__savings_at_year = savings_at_year
        self.__random_big_event = random_big_event
        self.__print_events = print_events

    @staticmethod
    def real_age(iter, curr_age):
        return curr_age+iter
    
    @staticmethod
    def inflation_adjusted(amount, inflation_rate, iter):
        return amount * (inflation_rate ** iter)
    
    @staticmethod
    def print_info(rate, savings, event, starting_amount, result, iter, curr_age, end_age):
        if (Events.real_age(iter, curr_age) == curr_age):
            print("\n%-3s    %-20s   %-4s   %-19s   %-21s   %-19s   %-20s" %
                  ("Age", "Starting Balance", 
                   "ROI", "Market Gain", "Expected Savings", 
                   "Random Event", "Net Gain"))
            
        savings_from_investments = (rate - 1) * starting_amount
        net = savings + savings_from_investments + event
        print("%-3.0f    %-20s   %-3.2f   %-20s  %-20s    %-20s  %-20s" % 
              (Events.real_age(iter, curr_age), format(starting_amount), rate, 
               format(savings_from_investments), format(savings), 
               format(event), format(net)))
        
        # to display the last year but not act on it
        if (Events.real_age(iter, curr_age) + 1 == end_age):
            print("%-3.0f    %-20s   " % 
              (Events.real_age(iter, curr_age) + 1, format(result)))
    
    def process_year(self, iter, starting_amount):
        rate = self.__random_rate(iter)
        savings = self.__savings_at_year(iter, curr_amount=starting_amount)
        event = self.__random_big_event(iter, curr_amount=starting_amount)
        result = (starting_amount * rate) + savings + event

        if self.__print_events:
            Events.print_info(rate=rate, 
                    savings=savings, 
                    event=event, 
                    starting_amount=starting_amount,
                    result=result,
                    iter=iter,
                    curr_age=self.__age,
                    end_age=self.__end_age)
        return result