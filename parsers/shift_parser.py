from datetime import datetime, timedelta
import re
from parsers.string_processor import String_processor

def datespan(startDate, endDate, delta):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

class ShiftParser:
    def __init__(self):
        self.labour_costs = {}

    def parse_timestamp(self, timestamp):
        for format in ('%H', '%H.%M', '%H:%M', '%I%p', '%I.%M%p', '%H ', ' %H'):
            try:
                return datetime.strptime(timestamp, format)
            except ValueError:
                pass
        raise ValueError('no valid date format found')

    def shift_start_end(self, entry_list):
        return {
            "shift_start": self.parse_timestamp(entry_list[3]),
            "shift_end": self.parse_timestamp(entry_list[1]),
        }

    def break_start_end(self, entry_list):
        break_start_end_list = self.separate_breaks(entry_list)
        return {
            "break_start": self.parse_timestamp(break_start_end_list[0]),
            "break_end": self.parse_timestamp(break_start_end_list[1]),
            }

    def separate_breaks(self, entry_list):
        split_breaks = entry_list[0].split("-")
        if 'PM' in split_breaks[1] and 'PM' not in split_breaks[0]:
            split_breaks[0] += 'PM'
        return split_breaks

    def align_breaks_with_shift(self, entry_list):
        shift_start_end = self.shift_start_end(entry_list)
        break_start_end = self.break_start_end(entry_list)

        if (shift_start_end["shift_start"] < break_start_end["break_start"] < break_start_end["break_end"] < shift_start_end["shift_end"]):
            pass
        else:
            break_start_end["break_start"] += timedelta(hours=12)
            break_start_end["break_end"] += timedelta(hours=12)
        return {
                "break_start": break_start_end["break_start"],
                "break_end": break_start_end["break_end"],
                "shift_start": shift_start_end["shift_start"],
                "shift_end": shift_start_end["shift_end"]
                }

    def extract_pay_rate(self, entry_list):
        pay_rate = float(entry_list[2])
        return pay_rate

    def extract_shift_data(self, entry_list):
        shift_and_break = self.align_breaks_with_shift(entry_list)
        pay_rate = {
            "pay_rate": self.extract_pay_rate(entry_list)
            }
        shift_data = {}
        shift_data.update(pay_rate)
        shift_data.update(shift_and_break)
        return shift_data

    def calculate_labour_cost_per_minute(self, work_start, work_end, pay_rate_per_minute):
        for minute in datespan(work_start, work_end, timedelta(minutes=1)):
            if minute.strftime("%H:00") not in self.labour_costs:
                self.labour_costs[minute.strftime("%H:00")] = 0.0
            self.labour_costs[minute.strftime("%H:00")] += pay_rate_per_minute

    def calculate_single_labour_costs(self, entry_list):
        shift_data = self.extract_shift_data(entry_list)
        pay_rate_per_minute = shift_data["pay_rate"]/60

        self.calculate_labour_cost_per_minute(shift_data["shift_start"], shift_data["break_start"],pay_rate_per_minute)
        self.calculate_labour_cost_per_minute(shift_data["break_end"], shift_data["shift_end"],pay_rate_per_minute)

        return self.labour_costs

    def round_costs(self):
        for labour_cost_per_hour in self.labour_costs:
            self.labour_costs[labour_cost_per_hour] = round(self.labour_costs[labour_cost_per_hour], 2)

    def total_labour_cost(self, string, processor = String_processor()):
        shifts_list = processor.process_string(string)
        for shift in shifts_list:
            self.calculate_single_labour_costs(shift)
        self.round_costs()
        return self.labour_costs
