from events_utils import Events


class Simulation:
    EventHelper = Events()
    def __init__(self, total_years, starting_amount):
        self.__total_years = total_years
        self.__starting_amount = starting_amount

    def single_simulation(self):
        results_per_year = []
        curr_saved = self.__starting_amount
        for year in range(self.__total_years):
            curr_saved = self.EventHelper.process_year(year=year, starting_amount=curr_saved)
            results_per_year.append(curr_saved)
        return results_per_year
    
    def many_simulations(self, number_of_simulations):
        for _ in range(number_of_simulations):
            yield self.single_simulation()

