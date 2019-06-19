def extract_data(full_string):
    return full_string.strip('break_notes,end_time,pay_rate,start_time\n')

def split_into_entries(extracted_data):
    return extracted_data.split("\n")
