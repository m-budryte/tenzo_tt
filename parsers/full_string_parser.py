from datetime import datetime, timedelta

day_labour_cost = {}
def extract_data(full_string):
    return full_string.strip('break_notes,end_time,pay_rate,start_time\n')

def split_into_entries(extracted_data):
    return extracted_data.split("\n")

def split_entry(entry):
    return entry.split(",")

def parse_start_end(entry_list):
    return {
        "shift_start": parse_timestamp(entry_list[3]),
        "shift_end": parse_timestamp(entry_list[1]),
    }

def separate_breaks(entry_list):
    split_breaks = entry_list[0].split("-")
    if 'PM' in split_breaks[1] and 'PM' not in split_breaks[0]:
        split_breaks[0] += 'PM'
    return split_breaks

def parse_timestamp(timestamp):
    for format in('%H', '%H.%M', '%H:%M', '%I%p', '%I.%M%p', '%H ', ' %H'):
        try:
            return datetime.strptime(timestamp, format)
        except ValueError:
            pass
    raise ValueError('no valid date format found')

def parse_break_start_end(break_start_end):
    return {
        "break_start": parse_timestamp(break_start_end[0]),
        "break_end": parse_timestamp(break_start_end[1]),
        }

def align_breaks(shift_start_end, break_start_end):
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

def datespan(startDate, endDate, delta):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

def calculate_costs(shift_data, rate):
    for hour in datespan(shift_data["shift_start"],shift_data["shift_end"],delta=timedelta(hours=1)):
        if hour.strftime('%H:%M') not in day_labour_cost:
            day_labour_cost[hour.strftime('%H:%M')] = 0
        day_labour_cost[hour.strftime('%H:%M')] += float(rate)
    for hour in datespan(shift_data["break_start"],shift_data["break_end"],delta=timedelta(hours=1)):
        day_labour_cost[hour.strftime('%H:%M')] -= float(rate)
    return day_labour_cost
