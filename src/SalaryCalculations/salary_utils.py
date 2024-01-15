from SalaryCalculations.salary import Salary


class SalaryUtils:
    @staticmethod
    def rent_to_recommended_salary(rent, roth_deductions):
        return SalaryUtils.__binary_search(target_rent=rent, roth_deductions=roth_deductions)
    
    @staticmethod
    def __binary_search(target_rent, roth_deductions, upper_bound=1_000_000_000):
        def close(num1, num2):
            return abs(num1 - num2) < 1
        low = 0
        high = upper_bound
        currSalary = Salary(salary=0, roth_deductions=roth_deductions)
        currRent = 0
        while (not close(currRent, target_rent)):
            mid = (low + high) >> 1
            currSalary = Salary(salary=-1, roth_deductions=roth_deductions, post_tax_semi_monthly=mid)
            currRent = currSalary.recommended_monthly_rent()
            if (currRent > target_rent):
                high = mid
            if (currRent < target_rent):
                low = mid
        return currSalary

