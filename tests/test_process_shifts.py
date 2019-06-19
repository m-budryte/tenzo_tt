import pytest
from datetime import datetime, timedelta
from pytest_fixtures import *
from parsers.full_string_parser import *

def test_extracts_data():
    assert extract_data(full_string) == extracted_data_string

def test_split_into_entries():
    assert split_into_entries(extracted_data_string) == [example_1, example_2, example_3, example_4, example_5, example_6, example_7]

def test_split_entry_1():
    assert split_entry(example_1) == ['15-18','23:00','10.0','10:00']

def test_parse_start_end_1():
    example_1_split = split_entry(example_1)
    assert parse_start_end(example_1_split) == {
        "shift_start": datetime(1900, 1, 1, 10, 0),
        "shift_end": datetime(1900, 1, 1, 23, 0),
    }

def test_separate_breaks_1():
    example_1_split = split_entry(example_1)
    assert separate_breaks(example_1_split) == ["15","18"]

def test_separate_breaks_2():
    example_2_split = split_entry(example_2)
    assert separate_breaks(example_2_split) == ["18.30","19.00"]

def test_separate_breaks_3():
    example_3_split = split_entry(example_3)
    assert separate_breaks(example_3_split) == ["4PM","5PM"]


example_1 = '15-18,23:00,10.0,10:00'
example_2 = '18.30-19.00,23:00,12.0,18:00'
example_3 = '4PM-5PM,22:30,14.0,12:00'
example_4 = '3-4,18:00,10.0,09:00'
example_5 = '4-4.10PM,23:00,20.0,09:00'
example_6 = '15 - 17,23:00,10.0,11:00'
example_7 = '11 - 13,16:00,10.0,10:00'

full_string = "break_notes,end_time,pay_rate,start_time\n15-18,23:00,10.0,10:00\n18.30-19.00,23:00,12.0,18:00\n4PM-5PM,22:30,14.0,12:00\n3-4,18:00,10.0,09:00\n4-4.10PM,23:00,20.0,09:00\n15 - 17,23:00,10.0,11:00\n11 - 13,16:00,10.0,10:00"

extracted_data_string = "15-18,23:00,10.0,10:00\n18.30-19.00,23:00,12.0,18:00\n4PM-5PM,22:30,14.0,12:00\n3-4,18:00,10.0,09:00\n4-4.10PM,23:00,20.0,09:00\n15 - 17,23:00,10.0,11:00\n11 - 13,16:00,10.0,10:00"
