from SalaryCalculations.salary import Salary


class SalaryUtils:
    @staticmethod
    def rent_to_recommended_salary(rent, roth_deductions, monthly_rent_percent, monthly_fun_percent, enable_tax_calculations=True):
        return SalaryUtils.__binary_search(target_rent=rent, 
                                           roth_deductions=roth_deductions, 
                                           monthly_rent_percent=monthly_rent_percent, 
                                           monthly_fun_percent=monthly_fun_percent,
                                           enable_tax_calculations=enable_tax_calculations)
    
    @staticmethod
    def __binary_search(target_rent, roth_deductions, monthly_rent_percent, monthly_fun_percent, enable_tax_calculations, upper_bound=1_000_000_000):
        def close(num1, num2):
            return abs(num1 - num2) < 1
        def getNewSalary(mid):
            if enable_tax_calculations:
                return Salary(salary=mid, 
                              roth_deductions=roth_deductions, 
                              monthly_rent_percent=monthly_rent_percent,
                              monthly_fun_percent=monthly_fun_percent)
            else:
                return Salary(salary="N/A", 
                              post_tax_semi_monthly=mid,
                              roth_deductions=roth_deductions, 
                              monthly_rent_percent=monthly_rent_percent,
                              monthly_fun_percent=monthly_fun_percent)
            
        low = 0
        high = upper_bound
        currSalary = Salary(salary=0, 
                            roth_deductions=roth_deductions, 
                            monthly_rent_percent=monthly_rent_percent,
                            monthly_fun_percent=monthly_fun_percent) 
        currRent = 0
        while (not close(currRent, target_rent)):
            mid = (low + high) >> 1
            currSalary = getNewSalary(mid=mid)
            currRent = currSalary.recommended_monthly_rent()
            if (currRent > target_rent):
                high = mid
            if (currRent < target_rent):
                low = mid
        return currSalary

