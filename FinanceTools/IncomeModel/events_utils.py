def format(num):
    return "${:,.2f}".format(num)


class Events:
    def __init__(
        self,
        curr_age,
        end_age,
        random_rate,
        savings_at_year,
        random_big_event,
        print_events=False,
    ):
        self.__age = curr_age
        self.__end_age = end_age
        self.__random_rate = random_rate
        self.__savings_at_year = savings_at_year
        self.__random_big_event = random_big_event
        self.__print_events = print_events

    @staticmethod
    def real_age(iter, curr_age):
        return curr_age + iter

    @staticmethod
    def inflation_adjusted(amount, inflation_rate, iter):
        return amount * (inflation_rate**iter)

    @staticmethod
    def print_info(
        rate, salary_obj, event, starting_amount, result, iter, curr_age, end_age
    ):
        if Events.real_age(iter, curr_age) == curr_age:
            print(
                "\n%-3s    %-20s   %-4s   %-19s   %-21s   %-19s   %-20s %-20s %-20s"
                % (
                    "Age",
                    "Starting Balance",
                    "ROI",
                    "Market Gain",
                    "Expected Savings",
                    "Random Event",
                    "Net Gain",
                    "Monthly Expense",
                    "Monthly Rent",
                )
            )

        savings_from_investments = (rate - 1) * starting_amount
        net = (
            salary_obj.recommended_yearly_savings(years=iter)
            + savings_from_investments
            + event
        )
        print(
            "%-3.0f    %-20s   %-3.2f   %-20s  %-20s    %-20s  %-20s %-20s %-20s"
            % (
                Events.real_age(iter, curr_age),
                format(starting_amount),
                rate,
                format(savings_from_investments),
                format(salary_obj.recommended_yearly_savings(years=iter)),
                format(event),
                format(net),
                format(salary_obj.monthly_fun(years=iter)),
                format(salary_obj.monthly_rent(years=iter)),
            )
        )

        # to display the last year but not act on it
        if Events.real_age(iter, curr_age) + 1 == end_age:
            print(
                "%-3.0f    %-20s   "
                % (Events.real_age(iter, curr_age) + 1, format(result))
            )

    def process_year(self, iter, starting_amount):
        rate = self.__random_rate(iter)
        salary_obj = self.__savings_at_year(iter)
        event = self.__random_big_event(iter, curr_amount=starting_amount)
        result = (
            (starting_amount * rate)
            + salary_obj.recommended_yearly_savings(years=0)
            + event
        )

        if self.__print_events:
            Events.print_info(
                rate=rate,
                salary_obj=salary_obj,
                event=event,
                starting_amount=starting_amount,
                result=result,
                iter=iter,
                curr_age=self.__age,
                end_age=self.__end_age,
            )
        return result
