class PercentageCalculator:
    def __init__(self, shifts, sales):
        self.labour = shifts
        self.sales = sales
        self.percentage_dict = {}
        self.percentage_dict.update(self.sales)

    def add_missing_time_keys(self):
        for timestamp in self.labour:
            if timestamp not in self.percentage_dict:
                self.percentage_dict[timestamp] = 0
        return self.percentage_dict
