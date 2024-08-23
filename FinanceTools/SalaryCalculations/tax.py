class Tax:
    __CONS_ADJUST = 1.00
    @staticmethod
    def federal_tax(salary):
        tax_bracket = [
            (10_275, .10),
            (41_775, .12),
            (89_075, .22),
            (170_050, .24),
            (215_950, .32),
            (539_900, .35),
            (float('inf'), .37)
        ]
        return Tax.__process_bracket(tax_bracket=tax_bracket, salary=salary)
    
    @staticmethod
    def state_tax_nyc(salary):
        tax_bracket = [
            (8_500, .04),
            (11_700, .045),
            (13_900, .0525),
            (80_650, .055),
            (215_400, .06),
            (1_077_550, .0685),
            (5_000_000, .0965),
            (25_000_000, .103),
            (float('inf'), .109)
        ]
        return Tax.__process_bracket(tax_bracket=tax_bracket, salary=salary)
    
    @staticmethod
    def city_tax_nyc(salary):
        tax_bracket = [
            (12_000, .03078),
            (25_000, .03762),
            (50_000, .03819),
            (float('inf'), .03876),            
        ]
        return Tax.__process_bracket(tax_bracket=tax_bracket, salary=salary)
    

    @staticmethod
    def __process_bracket(tax_bracket, salary):
        res = 0
        bucket_lower = 0
        for (bucket_upper, rate) in tax_bracket:
            to_tax = min(bucket_upper - bucket_lower, salary)
            res += (to_tax * rate)
            salary -= to_tax
            bucket_lower = bucket_upper
        return res
    
    @staticmethod
    def fica_and_state(salary):
        return 9114 + (salary * .015)
    
    @staticmethod
    def all_tax(salary):
        federal_tax = Tax.federal_tax(salary=salary)
        state_tax_nyc = Tax.state_tax_nyc(salary=salary)
        city_tax_nyc = Tax.city_tax_nyc(salary=salary)
        fica_and_state = Tax.fica_and_state(salary=salary)

        # print(f"Federal Tax:  {federal_tax / 24}")
        # print(f"State Tax:  {state_tax_nyc / 24}")
        # print(f"City Tax:  {city_tax_nyc / 24}")
        # print(f"Fica Tax:  {fica_and_state / 24}")

        return Tax.__CONS_ADJUST * (federal_tax + 
                                    state_tax_nyc + 
                                    city_tax_nyc + 
                                    fica_and_state)
