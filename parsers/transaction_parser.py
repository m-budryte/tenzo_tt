from datetime import datetime, timedelta
from parsers.string_processor import String_processor

class TransactionParser:
    def __init__(self):
        self.day_profit = {}

    def parse_timestamp(self, string):
        return datetime.strptime(string, "%H:%M")

    def parse_profit(self, string):
        return float(string)

    def round_profits(self):
        for labour_cost_per_hour in self.day_profit:
            self.day_profit[labour_cost_per_hour] = round(self.day_profit[labour_cost_per_hour], 2)

    def calculate_profit(self, string, processor = String_processor()):
        transaction_list = processor.process_string(string)
        for transaction in transaction_list:
            timestamp = self.parse_timestamp(transaction[1])
            amount = self.parse_profit(transaction[0])
            if timestamp.strftime("%H:00") not in self.day_profit:
                self.day_profit[timestamp.strftime("%H:00")] = 0.0
            self.day_profit[timestamp.strftime("%H:00")] += amount
        self.round_profits()
        return self.day_profit
