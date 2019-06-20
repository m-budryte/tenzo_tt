import pytest
from datetime import datetime, timedelta
from parsers.transaction_parser import TransactionParser
from pytest_fixtures import *

class TestParsingTimestamp:
    parser = TransactionParser()
    def test_parse_timestamp(self):
        assert self.parser.parse_timestamp('10:00') == datetime(1900, 1, 1, 10, 0)

    def test_parse_timestamp(self):
        assert self.parser.parse_timestamp('22:13') == datetime(1900, 1, 1, 22, 13)


class TestParsingProfit:
    parser = TransactionParser()
    def test_parse_timestamp(self):
        assert self.parser.parse_profit("100.32") == 100.32
    def test_parse_timestamp(self):
        assert self.parser.parse_profit("30.56") == 30.56

class TestProfit:
    parser = TransactionParser()
    def test_calculate_profit(self):
        assert self.parser.calculate_profit(full_string) == {'11:00': 320.65, '10:00': 130.88}


full_string = "amount,time\n100.32,10:31\n30.56,10:56\n300.65,11:05\n20.0,11:31"
extracted_data_string = "100.32,10:31\n30.56,10:56\n300.65,11:05\n20.0,11:31"
