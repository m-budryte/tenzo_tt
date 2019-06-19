from datetime import datetime, timedelta

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
    return entry_list[0].split("-")

def parse_timestamp(timestamp):
    for format in('%H', '%H.%M', '%H:%M', '%I%p'):
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
