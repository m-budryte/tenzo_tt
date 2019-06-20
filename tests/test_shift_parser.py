import pytest
from datetime import datetime, timedelta
from pytest_fixtures import *
from parsers.shift_parser import Shift_parser

parser = Shift_parser()

def test_parse_timestamp_1():
    assert parser.parse_timestamp('10:00') == datetime(1900, 1, 1, 10, 0)

def test_parse_timestamp_2():
    assert parser.parse_timestamp('4') == datetime(1900, 1, 1, 4, 0)

def test_parse_timestamp_3():
    assert parser.parse_timestamp('4PM') == datetime(1900, 1, 1, 16, 0)

def test_parse_timestamp_4():
    assert parser.parse_timestamp('14.45') == datetime(1900, 1, 1, 14, 45)

def test_parse_timestamp_5():
    assert parser.parse_timestamp('17 ') == datetime(1900, 1, 1, 17, 0)

def test_parse_timestamp_6():
    assert parser.parse_timestamp(' 15') == datetime(1900, 1, 1, 15, 0)

def test_shift_start_end_1():
    assert parser.shift_start_end(example_1) == {
        "shift_start": datetime(1900, 1, 1, 10, 0),
        "shift_end": datetime(1900, 1, 1, 23, 0),
    }

def test_shift_start_end_2():
    assert parser.shift_start_end(example_2) == {
        "shift_start": datetime(1900, 1, 1, 18, 0),
        "shift_end": datetime(1900, 1, 1, 23, 0),
    }

def test_separate_breaks_1():
    assert parser.separate_breaks(example_1) == ['15','18']

def test_separate_breaks_2():
    assert parser.separate_breaks(example_2) == ['18.30','19.00']

def test_separate_breaks_2():
    assert parser.separate_breaks(example_5) == ['4PM','4.10PM']

def test_break_start_end_1():
    assert parser.break_start_end(example_1) == {
        "break_start": datetime(1900, 1, 1, 15, 0),
        "break_end": datetime(1900, 1, 1, 18, 0),
        }

def test_break_start_end_2():
    assert parser.break_start_end(example_2) == {
        "break_start": datetime(1900, 1, 1, 18, 30),
        "break_end": datetime(1900, 1, 1, 19, 0),
        }

def test_break_start_end_3():
    assert parser.break_start_end(example_3) == {
        "break_start": datetime(1900, 1, 1, 16, 0),
        "break_end": datetime(1900, 1, 1, 17, 0),
        }

def test_break_start_end_4():
    assert parser.break_start_end(example_4) == {
        "break_start": datetime(1900, 1, 1, 3, 0),
        "break_end": datetime(1900, 1, 1, 4, 0),
        }

def test_break_start_end_5():
    assert parser.break_start_end(example_5) == {
        "break_start": datetime(1900, 1, 1, 16, 0),
        "break_end": datetime(1900, 1, 1, 16, 10),
        }

def test_break_start_end_6():
    assert parser.break_start_end(example_6) == {
        "break_start": datetime(1900, 1, 1, 15, 0),
        "break_end": datetime(1900, 1, 1, 17, 0),
        }

def test_break_start_end_7():
    assert parser.break_start_end(example_7) == {
        "break_start": datetime(1900, 1, 1, 11, 0),
        "break_end": datetime(1900, 1, 1, 13, 0),
        }

def test_aling_breaks_1():
    assert parser.align_breaks_with_shift(example_1) == {
            "break_start": datetime(1900, 1, 1, 15, 0),
            "break_end": datetime(1900, 1, 1, 18, 0),
            "shift_start": datetime(1900, 1, 1, 10, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0)
    }


def test_aling_breaks_2():
    assert parser.align_breaks_with_shift(example_2) == {
            "break_start": datetime(1900, 1, 1, 18, 30),
            "break_end": datetime(1900, 1, 1, 19, 0),
            "shift_start": datetime(1900, 1, 1, 18, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0)
    }

def test_aling_breaks_3():
    assert parser.align_breaks_with_shift(example_3) == {
            "break_start": datetime(1900, 1, 1, 16, 0),
            "break_end": datetime(1900, 1, 1, 17, 0),
            "shift_start": datetime(1900, 1, 1, 12, 0),
            "shift_end": datetime(1900, 1, 1, 22, 30)
    }
def test_aling_breaks_4():
    assert parser.align_breaks_with_shift(example_4) == {
            "break_start": datetime(1900, 1, 1, 15, 0),
            "break_end": datetime(1900, 1, 1, 16, 0),
            "shift_start": datetime(1900, 1, 1, 9, 0),
            "shift_end": datetime(1900, 1, 1, 18, 0)
    }

def test_aling_breaks_5():
    assert parser.align_breaks_with_shift(example_5) == {
            "break_start": datetime(1900, 1, 1, 16, 0),
            "break_end": datetime(1900, 1, 1, 16, 10),
            "shift_start": datetime(1900, 1, 1, 9, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0)
    }

def test_aling_breaks_6():
    assert parser.align_breaks_with_shift(example_6) == {
            "break_start": datetime(1900, 1, 1, 15, 0),
            "break_end": datetime(1900, 1, 1, 17, 0),
            "shift_start": datetime(1900, 1, 1, 11, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0)
    }

def test_aling_breaks_7():
    assert parser.align_breaks_with_shift(example_7) == {
        "break_start": datetime(1900, 1, 1, 11, 0),
        "break_end": datetime(1900, 1, 1, 13, 0),
        "shift_start": datetime(1900, 1, 1, 10, 0),
        "shift_end": datetime(1900, 1, 1, 16, 0)
        }
def test_extract_pay_rate_1():
    assert parser.extract_pay_rate(example_1) == 10.0

def test_extract_pay_rate_2():
    assert parser.extract_pay_rate(example_2) == 12.0

def test_extract_pay_rate_3():
    assert parser.extract_pay_rate(example_3) == 14.0

def test_extract_pay_rate_4():
    assert parser.extract_pay_rate(example_4) == 10.0

def test_extract_pay_rate_5():
    assert parser.extract_pay_rate(example_5) == 20.0

def test_extract_shift_data_1():
    assert parser.extract_shift_data(example_1) == {
            "break_start": datetime(1900, 1, 1, 15, 0),
            "break_end": datetime(1900, 1, 1, 18, 0),
            "shift_start": datetime(1900, 1, 1, 10, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0),
            "pay_rate": 10.0
            }

def test_extract_shift_data_2():
    assert parser.extract_shift_data(example_2) == {
            "break_start": datetime(1900, 1, 1, 18, 30),
            "break_end": datetime(1900, 1, 1, 19, 0),
            "shift_start": datetime(1900, 1, 1, 18, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0),
            "pay_rate": 12.0
            }

example_1 = ['15-18','23:00','10.0','10:00']
example_2 = ['18.30-19.00','23:00','12.0','18:00']
example_3 = ['4PM-5PM','22:30','14.0','12:00']
example_4 = ['3-4','18:00','10.0','09:00']
example_5 = ['4-4.10PM','23:00','20.0','09:00']
example_6 = ['15 - 17','23:00','10.0','11:00']
example_7 = ['11 - 13','16:00','10.0','10:00']


full_string = "break_notes,end_time,pay_rate,start_time\n15-18,23:00,10.0,10:00\n18.30-19.00,23:00,12.0,18:00\n4PM-5PM,22:30,14.0,12:00\n3-4,18:00,10.0,09:00\n4-4.10PM,23:00,20.0,09:00\n15 - 17,23:00,10.0,11:00\n11 - 13,16:00,10.0,10:00"
parsed_string = [example_1, example_2, example_3, example_4, example_5, example_6, example_7]
