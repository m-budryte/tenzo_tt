import pytest
from datetime import datetime, timedelta
from parsers.calculators.percentage_calculator import PercentageCalculator

class TestFullTimesDictCreated:
    def test_add_missing_time_keys_1(self):
        calculator = PercentageCalculator(equal_pay_day_with_equality_bonus,evening_party)
        assert calculator.add_missing_time_keys() == {
            "09:00": 0.0,
            "10:00": 0.0,
            "11:00": 0.0,
            "12:00": 0.0,
            "13:00": 0.0,
            "14:00": 0.0,
            "15:00": 0.0,
            "16:00": 0.0,
            "17:00": 0.0,
            "18:00": 10.0,
            "19:00": 10.0,
            "20:00": 10.0,
            "21:00": 10.0,
        }

    def test_add_missing_time_keys_1(self):
        calculator = PercentageCalculator(everyone_unpaid,evening_party)
        assert calculator.add_missing_time_keys() == {
            "18:00": 10.0,
            "19:00": 10.0,
            "20:00": 10.0,
            "21:00": 10.0,
        }
# LABOUR
everyone_unpaid = {}

paid_after_hours = {
    "18:00": 100.0,
    "19:00": 100.0,
    "20:00": 100.0,
    "21:00": 100.0,
}

equal_pay_day_with_equality_bonus = {
    "09:00": 100.0,
    "10:00": 100.0,
    "11:00": 100.0,
    "12:00": 100.0,
    "13:00": 100.0,
    "14:00": 100.0,
    "15:00": 100.0,
    "16:00": 100.0,
    "17:00": 100.0,
}
normal_day = {
    "09:00": 10.0,
    "10:00": 20.0,
    "11:00": 30.0,
    "12:00": 30.0,
    "13:00": 30.0,
    "14:00": 30.0,
    "15:00": 20.0,
    "16:00": 20.0,
    "17:00": 10.0,
}

# SALES

dry_county = {}
christmas = {
    "09:00": 10.0,
    "10:00": 20.0,
    "11:00": 30.0,
    "12:00": 40.0,
    "13:00": 50.0,
    "14:00": 60.0,
    "15:00": 70.0,
    "16:00": 70.0,
    "17:00": 70.0,
}

evening_party = {
    "18:00": 10.0,
    "19:00": 10.0,
    "20:00": 10.0,
    "21:00": 10.0,
}
