import pytest
from parsers.string_processor import String_processor
from pytest_fixtures import *

processor = String_processor()

def test_remove_first_line():
    assert processor.remove_first_line(full_string) == extracted_data_string

def test_split_into_entries():
    assert processor.split_into_entries(full_string) == entries

def test_split_into_entries():
    assert processor.split_into_entries(full_string) == entries

def test_split_entry():
    assert processor.split_entry(example_1) == ['15-18','23:00','10.0','10:00']

def test_process_string():
    assert processor.process_string(full_string) == [['15-18', '23:00', '10.0', '10:00'], ['18.30-19.00', '23:00', '12.0', '18:00'], ['4PM-5PM', '22:30', '14.0', '12:00'], ['3-4', '18:00', '10.0', '09:00'], ['4-4.10PM', '23:00', '20.0', '09:00'], ['15 - 17', '23:00', '10.0', '11:00'], ['11 - 13', '16:00', '10.0', '10:00']]

example_1 = '15-18,23:00,10.0,10:00'
example_2 = '18.30-19.00,23:00,12.0,18:00'
example_3 = '4PM-5PM,22:30,14.0,12:00'
example_4 = '3-4,18:00,10.0,09:00'
example_5 = '4-4.10PM,23:00,20.0,09:00'
example_6 = '15 - 17,23:00,10.0,11:00'
example_7 = '11 - 13,16:00,10.0,10:00'

full_string = "break_notes,end_time,pay_rate,start_time\n15-18,23:00,10.0,10:00\n18.30-19.00,23:00,12.0,18:00\n4PM-5PM,22:30,14.0,12:00\n3-4,18:00,10.0,09:00\n4-4.10PM,23:00,20.0,09:00\n15 - 17,23:00,10.0,11:00\n11 - 13,16:00,10.0,10:00"

extracted_data_string = "15-18,23:00,10.0,10:00\n18.30-19.00,23:00,12.0,18:00\n4PM-5PM,22:30,14.0,12:00\n3-4,18:00,10.0,09:00\n4-4.10PM,23:00,20.0,09:00\n15 - 17,23:00,10.0,11:00\n11 - 13,16:00,10.0,10:00"

entries = [example_1, example_2, example_3, example_4, example_5, example_6, example_7]
