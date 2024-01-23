from IncomeModel.events_utils import Events


class Simulation:
    def __init__(self, starting_amount, curr_age, end_age, random_rate, savings_at_year, random_big_event):
        self.__total_years = end_age - curr_age + 1
        self.__starting_amount = starting_amount
        self.__event_helper = Events(curr_age=23,
                                     random_rate=random_rate, 
                                     savings_at_year=savings_at_year, 
                                     random_big_event=random_big_event)

    def single_simulation(self):
        results_per_year = [self.__starting_amount]
        curr_saved = self.__starting_amount
        success = True
        for year in range(self.__total_years):
            curr_saved = max(self.__event_helper.process_year(
                            year=year, starting_amount=curr_saved), 0)
            results_per_year.append(curr_saved)
            if (curr_saved <= 0): success = False
        return (results_per_year, success)
    
    def many_simulations(self, number_of_simulations):
        for _ in range(number_of_simulations):
            yield self.single_simulation()

