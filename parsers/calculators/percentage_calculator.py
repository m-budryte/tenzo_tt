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
                self.percentage_dict[timestamp] = -self.labour[timestamp]
        return self.percentage_dict

    def round_numbers(self):
        for number in self.percentage_dict:
            self.percentage_dict[number] = round(self.percentage_dict[number], 1)

    def calculate_percentage(self):
        self.add_missing_time_keys()
        for timestamp in self.percentage_dict:
            percentage = self.labour[timestamp]*100/self.percentage_dict[timestamp]
            if self.percentage_dict[timestamp] > 0:
                self.percentage_dict[timestamp] = percentage
        self.round_numbers()
        print(self.percentage_dict)
        return self.percentage_dict
