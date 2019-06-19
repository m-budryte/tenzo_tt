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
    example_split = split_entry(example_1)
    assert separate_breaks(example_split) == ["15","18"]

def test_separate_breaks_2():
    example_split = split_entry(example_2)
    assert separate_breaks(example_split) == ["18.30","19.00"]

def test_separate_breaks_3():
    example_split = split_entry(example_3)
    assert separate_breaks(example_split) == ["4PM","5PM"]

def test_parse_timestamp_1():
    example_split = split_entry(example_1)
    break_start_end = separate_breaks(example_split)
    break_start = break_start_end[0]
    break_end = break_start_end[1]
    assert parse_timestamp(break_start) == datetime(1900, 1, 1, 15, 0)
    assert parse_timestamp(break_end) == datetime(1900, 1, 1, 18, 0)

def test_parse_timestamp_2():
    example_split = split_entry(example_2)
    break_start_end = separate_breaks(example_split)
    break_start = break_start_end[0]
    break_end = break_start_end[1]
    assert parse_timestamp(break_start) == datetime(1900, 1, 1, 18, 30)
    assert parse_timestamp(break_end) == datetime(1900, 1, 1, 19, 0)

def test_parse_timestamp_3():
    example_split = split_entry(example_3)
    break_start_end = separate_breaks(example_split)
    break_start = break_start_end[0]
    break_end = break_start_end[1]
    assert parse_timestamp(break_start) == datetime(1900, 1, 1, 16, 0)
    assert parse_timestamp(break_end) == datetime(1900, 1, 1, 17, 0)

def test_parse_timestamp_4():
    example_split = split_entry(example_4)
    break_start_end = separate_breaks(example_split)
    break_start = break_start_end[0]
    break_end = break_start_end[1]
    assert parse_timestamp(break_start) == datetime(1900, 1, 1, 3, 0)
    assert parse_timestamp(break_end) == datetime(1900, 1, 1, 4, 0)

def test_parse_break_start_end_1():
    example_split = split_entry(example_1)
    break_start_end = separate_breaks(example_split)
    assert parse_break_start_end(break_start_end) == {
        "break_start": datetime(1900, 1, 1, 15, 0),
        "break_end": datetime(1900, 1, 1, 18, 0),
    }

def test_parse_break_start_end_4():
    example_split = split_entry(example_4)
    break_start_end = separate_breaks(example_split)
    assert parse_break_start_end(break_start_end) == {
        "break_start": datetime(1900, 1, 1, 3, 0),
        "break_end": datetime(1900, 1, 1, 4, 0),
    }

def test_aling_breaks_1():
    example_split = split_entry(example_1)
    break_start_end = separate_breaks(example_split)
    parsed_break_data = parse_break_start_end(break_start_end)
    parsed_shift_data = parse_start_end(example_split)
    assert align_breaks(parsed_shift_data, parsed_break_data) == [datetime(1900, 1, 1, 15, 0), datetime(1900, 1, 1, 18, 0), datetime(1900, 1, 1, 10, 0), datetime(1900, 1, 1, 23, 0)]

def test_aling_breaks_2():
    example_split = split_entry(example_2)
    break_start_end = separate_breaks(example_split)
    parsed_break_data = parse_break_start_end(break_start_end)
    parsed_shift_data = parse_start_end(example_split)
    assert align_breaks(parsed_shift_data, parsed_break_data) == [datetime(1900, 1, 1, 18, 30), datetime(1900, 1, 1, 19, 0), datetime(1900, 1, 1, 18, 0), datetime(1900, 1, 1, 23, 0)]

def test_aling_breaks_3():
    example_split = split_entry(example_3)
    break_start_end = separate_breaks(example_split)
    parsed_break_data = parse_break_start_end(break_start_end)
    parsed_shift_data = parse_start_end(example_split)
    assert align_breaks(parsed_shift_data, parsed_break_data) == [datetime(1900, 1, 1, 16, 0), datetime(1900, 1, 1, 17, 0), datetime(1900, 1, 1, 12, 0), datetime(1900, 1, 1, 22, 30)]

def test_aling_breaks_4():
    example_split = split_entry(example_4)
    break_start_end = separate_breaks(example_split)
    parsed_break_data = parse_break_start_end(break_start_end)
    parsed_shift_data = parse_start_end(example_split)
    assert align_breaks(parsed_shift_data, parsed_break_data) == [datetime(1900, 1, 1, 15, 0), datetime(1900, 1, 1, 16, 0), datetime(1900, 1, 1, 9, 0), datetime(1900, 1, 1, 18, 0)]

def test_aling_breaks_5():
    example_split = split_entry(example_5)
    break_start_end = separate_breaks(example_split)
    parsed_break_data = parse_break_start_end(break_start_end)
    parsed_shift_data = parse_start_end(example_split)
    assert align_breaks(parsed_shift_data, parsed_break_data) == [datetime(1900, 1, 1, 16, 0), datetime(1900, 1, 1, 16, 10), datetime(1900, 1, 1, 9, 0), datetime(1900, 1, 1, 23, 0)]

def test_aling_breaks_6():
    example_split = split_entry(example_6)
    break_start_end = separate_breaks(example_split)
    parsed_break_data = parse_break_start_end(break_start_end)
    parsed_shift_data = parse_start_end(example_split)
    assert align_breaks(parsed_shift_data, parsed_break_data) == [datetime(1900, 1, 1, 15, 0), datetime(1900, 1, 1, 17, 0), datetime(1900, 1, 1, 11, 0), datetime(1900, 1, 1, 23, 0)]

def test_aling_breaks_7():
    example_split = split_entry(example_7)
    break_start_end = separate_breaks(example_split)
    parsed_break_data = parse_break_start_end(break_start_end)
    parsed_shift_data = parse_start_end(example_split)
    assert align_breaks(parsed_shift_data, parsed_break_data) == [datetime(1900, 1, 1, 11, 0), datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 10, 0), datetime(1900, 1, 1, 16, 0)]

example_1 = '15-18,23:00,10.0,10:00'
example_2 = '18.30-19.00,23:00,12.0,18:00'
example_3 = '4PM-5PM,22:30,14.0,12:00'
example_4 = '3-4,18:00,10.0,09:00'
example_5 = '4-4.10PM,23:00,20.0,09:00'
example_6 = '15 - 17,23:00,10.0,11:00'
example_7 = '11 - 13,16:00,10.0,10:00'

full_string = "break_notes,end_time,pay_rate,start_time\n15-18,23:00,10.0,10:00\n18.30-19.00,23:00,12.0,18:00\n4PM-5PM,22:30,14.0,12:00\n3-4,18:00,10.0,09:00\n4-4.10PM,23:00,20.0,09:00\n15 - 17,23:00,10.0,11:00\n11 - 13,16:00,10.0,10:00"

extracted_data_string = "15-18,23:00,10.0,10:00\n18.30-19.00,23:00,12.0,18:00\n4PM-5PM,22:30,14.0,12:00\n3-4,18:00,10.0,09:00\n4-4.10PM,23:00,20.0,09:00\n15 - 17,23:00,10.0,11:00\n11 - 13,16:00,10.0,10:00"
