from FinanceTools.IncomeModel.events_utils import Events

class Simulation:
    def __init__(self, starting_amount, curr_age, end_age, random_rate, savings_at_year, random_big_event, print_events=False):
        assert(end_age > curr_age)
        self.__curr_age = curr_age
        self.__total_iters = end_age - curr_age
        self.__starting_amount = starting_amount
        self.__event_helper = Events(curr_age=curr_age,
                                     end_age=end_age,
                                     random_rate=random_rate, 
                                     savings_at_year=savings_at_year, 
                                     random_big_event=random_big_event,
                                     print_events=print_events)

    def get_total_iters(self):
        return self.__total_iters
    
    def get_starting_age(self):
        return self.__curr_age
    
    def single_simulation(self):
        results_per_year = [self.__starting_amount]
        curr_saved = self.__starting_amount
        success = True
        for iter in range(0, self.__total_iters):
            curr_saved = max(self.__event_helper.process_year(
                            iter=iter, starting_amount=curr_saved), 0)
            results_per_year.append(curr_saved)
        if (curr_saved <= 0): success = False
        return (results_per_year, success)
    
    def many_simulations(self, number_of_simulations):
        for _ in range(number_of_simulations):
            yield self.single_simulation()
    