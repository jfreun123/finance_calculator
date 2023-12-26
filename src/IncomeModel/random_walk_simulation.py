from IncomeModel.events_utils import Events


class Simulation:
    def __init__(self, end_age, starting_amount, retirement_age, inflation, curr_age):
        self.__total_years = end_age - curr_age + 1
        self.__starting_amount = starting_amount
        self.__event_helper = Events(retirement_age=retirement_age, inflation=inflation, curr_age=curr_age)

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

