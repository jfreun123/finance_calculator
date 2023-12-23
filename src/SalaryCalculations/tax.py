class Tax:
    
    @staticmethod
    def federal_tax(salary):
        tax_bracket = [
            (11_000, .10),
            (44_725, .12),
            (95_375, .22),
            (182_100, .24),
            (231_250, .32),
            (578_125, .35),
            (float('inf'), 37)
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
        for (bucket, rate) in tax_bracket:
            to_tax = min(bucket, salary)
            res += (to_tax * rate)
            salary -= to_tax
        return res
    
    @staticmethod
    def fica_and_state(salary):
        return 9114 + (salary * .025)
    
    @staticmethod
    def all_tax(salary):
        federal_tax = Tax.federal_tax(salary=salary)
        state_tax_nyc = Tax.state_tax_nyc(salary=salary)
        city_tax_nyc = Tax.city_tax_nyc(salary=salary)
        fica_and_state = Tax.fica_and_state(salary=salary)
        return federal_tax + state_tax_nyc + city_tax_nyc + fica_and_state
