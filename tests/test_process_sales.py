import pytest
from datetime import datetime, timedelta
from solution.solution import *
from parsers.transactions_parser import *
from pytest_fixtures import *

def test_extracts_data():
    assert extract_data(full_string) == extracted_data_string

def test_split_into_entries():
    assert split_into_entries(extracted_data_string) == [example_1, example_2, example_3, example_4]

def test_split_entry_1():
    assert split_entry(example_1) == ["100.32","10:31"]

def test_parse_timestamp_1():
    example_split = split_entry(example_1)
    assert parse_timestamp(example_split) == datetime(1900, 1, 1, 10, 31)

def test_parse_profit_1():
    example_split = split_entry(example_1)
    assert parse_profit(example_split) == 100.32

def test_calculate_profits():
    assert calculate_profits(full_string) == {'10:00': 130.88, '11:00': 320.65}

def test_process_sales():
    assert process_sales('transactions.csv') == {
    '10:00': 261.76,
    '11:00': 641.3,
    '12:00': 514.65,
    '13:00': 406.08000000000004,
    '14:00': 177.77,
    '15:00': 63.43,
    '16:00': 75.42,
    '17:00': 142.34,
    '18:00': 748.62,
    '19:00': 421.08,
    '21:00': 240.54
    }

full_string = "amount,time\n100.32,10:31\n30.56,10:56\n300.65,11:05\n20.0,11:31"
extracted_data_string = "100.32,10:31\n30.56,10:56\n300.65,11:05\n20.0,11:31"
example_1 = "100.32,10:31"
example_2 = "30.56,10:56"
example_3 = "300.65,11:05"
example_4 = "20.0,11:31"
