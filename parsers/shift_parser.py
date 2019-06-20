from datetime import datetime, timedelta
import re

day_labour_cost = {}

class Shift_parser:
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
