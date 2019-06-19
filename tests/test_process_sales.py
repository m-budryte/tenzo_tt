import pytest
from datetime import datetime, timedelta
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

full_string = "amount,time\n100.32,10:31\n30.56,10:56\n300.65,11:05\n20.0,11:31"
extracted_data_string = "100.32,10:31\n30.56,10:56\n300.65,11:05\n20.0,11:31"
example_1 = "100.32,10:31"
example_2 = "30.56,10:56"
example_3 = "300.65,11:05"
example_4 = "20.0,11:31"
"""

:param path_to_csv: The path to the transactions.csv
:type string:
:return: A dictionary with time (string) with format %H:%M as key and
sales as value (string),
and corresponding value with format %H:%M (e.g. "18:00"),
and type float)
For example, it should be something like :
{
    "17:00": 250,
    "22:00": 0,
},
This means, for the hour beginning at 17:00, the sales were 250 dollars
and for the hour beginning at 22:00, the sales were 0.

:rtype dict:
"""
