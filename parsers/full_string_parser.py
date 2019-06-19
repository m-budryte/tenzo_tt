from datetime import datetime, timedelta

def extract_data(full_string):
    return full_string.strip('break_notes,end_time,pay_rate,start_time\n')

def split_into_entries(extracted_data):
    return extracted_data.split("\n")

def split_entry(entry):
    return entry.split(",")

def parse_start_end(entry_list):
    return {
        "shift_start": datetime.strptime(entry_list[3], "%H:%M"),
        "shift_end": datetime.strptime(entry_list[1], "%H:%M"),
    }

def separate_breaks(entry_list):
    return entry_list[0].split("-")

def try_parsing_timestamp(timestamp):
    for format in('%H', '%H:%M'):
        try:
            return datetime.strptime(timestamp, format)
        except ValueError:
            pass
    raise ValueError('no valid date format found')
