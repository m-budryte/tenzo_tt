from datetime import datetime, timedelta

day_profit = {}
def extract_data(full_string):
    return full_string.strip('amount,time\n')

def split_into_entries(extracted_data):
    return extracted_data.split("\n")

def split_entry(entry):
    return entry.split(",")

def parse_timestamp(entry):
    return datetime.strptime(entry[1], "%H:%M")

def parse_profit(entry):
    return float(entry[0])

def datespan(startDate, endDate, delta):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta

def calculate_profits(string):
    data = extract_data(string)
    entries = split_into_entries(data)
    for entry in entries:
        entry = split_entry(entry)
        timestamp = parse_timestamp(entry)
        profit = parse_profit(entry)
        if timestamp.strftime('%H:00') not in day_profit:
            day_profit[timestamp.strftime('%H:00')] = 0

        day_profit[timestamp.strftime('%H:00')] += profit
    return day_profit
