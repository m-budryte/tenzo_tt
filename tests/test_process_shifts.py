import pytest
from solution.solution import *
from pytest_fixtures import *
from parsers.work_shifts_parser import Work_shifts_parser

def test_process_shifts():
    assert process_shifts('work_shifts.csv') == {
    '09:00': 30.0,
    '10:00': 50.0,
    '11:00': 50.0,
    '12:00': 64.0,
    '13:00': 74.0,
    '14:00': 74.0,
    '15:00': 44.0,
    '16:00': 26.67,
    '17:00': 54.0,
    '18:00': 60.0,
    '19:00': 66.0,
    '20:00': 66.0,
    '22:00': 59.0,
    '21:00': 66.0,
    '20:00': 66.0,
    }
