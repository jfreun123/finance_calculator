from events_utils import Events


class Simulation:
    EventHelper = Events()
    def single_simulation(self, total_years, starting_amount):
        results_per_year = []
        curr_saved = starting_amount
        for year in range(total_years):
            curr_saved = self.EventHelper.process_year(year=year, starting_amount=curr_saved)
            results_per_year.append(curr_saved)
        return results_per_year
    
    def many_simulations(self, total_years, starting_amount, number_of_simulations):
        for _ in range(number_of_simulations):
            yield self.single_simulation(total_years=total_years, 
                                         starting_amount=starting_amount)

