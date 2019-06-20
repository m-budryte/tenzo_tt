import pytest
from datetime import datetime, timedelta
from pytest_fixtures import *
from parsers.shift_parser import ShiftParser
class TestParsingTimestamps:
    parser = ShiftParser()
    def test_parse_timestamp_1(self):
        assert self.parser.parse_timestamp('10:00') == datetime(1900, 1, 1, 10, 0)

    def test_parse_timestamp_2(self):
        assert self.parser.parse_timestamp('4') == datetime(1900, 1, 1, 4, 0)

    def test_parse_timestamp_3(self):
        assert self.parser.parse_timestamp('4PM') == datetime(1900, 1, 1, 16, 0)

    def test_parse_timestamp_4(self):
        assert self.parser.parse_timestamp('14.45') == datetime(1900, 1, 1, 14, 45)

    def test_parse_timestamp_5(self):
        assert self.parser.parse_timestamp('17 ') == datetime(1900, 1, 1, 17, 0)

    def test_parse_timestamp_6(self):
        assert self.parser.parse_timestamp(' 15') == datetime(1900, 1, 1, 15, 0)

class TestParsingShiftStartEnd:
    parser = ShiftParser()

    def test_shift_start_end_1(self):
        assert self.parser.shift_start_end(example_1) == {
            "shift_start": datetime(1900, 1, 1, 10, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0),
        }

    def test_shift_start_end_2(self):
        assert self.parser.shift_start_end(example_2) == {
            "shift_start": datetime(1900, 1, 1, 18, 0),
            "shift_end": datetime(1900, 1, 1, 23, 0),
        }

class TestSeparatingBreaks:
    parser = ShiftParser()

    def test_separate_breaks_1(self):
        assert self.parser.separate_breaks(example_1) == ['15','18']

    def test_separate_breaks_2(self):
        assert self.parser.separate_breaks(example_2) == ['18.30','19.00']

    def test_separate_breaks_2(self):
        assert self.parser.separate_breaks(example_5) == ['4PM','4.10PM']

class TestParsingBreaks:
    parser = ShiftParser()
    def test_break_start_end_1(self):
        assert self.parser.break_start_end(example_1) == {
            "break_start": datetime(1900, 1, 1, 15, 0),
            "break_end": datetime(1900, 1, 1, 18, 0),
            }

    def test_break_start_end_2(self):
        assert self.parser.break_start_end(example_2) == {
            "break_start": datetime(1900, 1, 1, 18, 30),
            "break_end": datetime(1900, 1, 1, 19, 0),
            }

    def test_break_start_end_3(self):
        assert self.parser.break_start_end(example_3) == {
            "break_start": datetime(1900, 1, 1, 16, 0),
            "break_end": datetime(1900, 1, 1, 17, 0),
            }

    def test_break_start_end_4(self):
        assert self.parser.break_start_end(example_4) == {
            "break_start": datetime(1900, 1, 1, 3, 0),
            "break_end": datetime(1900, 1, 1, 4, 0),
            }

    def test_break_start_end_5(self):
        assert self.parser.break_start_end(example_5) == {
            "break_start": datetime(1900, 1, 1, 16, 0),
            "break_end": datetime(1900, 1, 1, 16, 10),
            }

    def test_break_start_end_6(self):
        assert self.parser.break_start_end(example_6) == {
            "break_start": datetime(1900, 1, 1, 15, 0),
            "break_end": datetime(1900, 1, 1, 17, 0),
            }

    def test_break_start_end_7(self):
        assert self.parser.break_start_end(example_7) == {
            "break_start": datetime(1900, 1, 1, 11, 0),
            "break_end": datetime(1900, 1, 1, 13, 0),
            }

class TestAligningBreaks:
    parser = ShiftParser()
    def test_aling_breaks_1(self):
        assert self.parser.align_breaks_with_shift(example_1) == {
                "break_start": datetime(1900, 1, 1, 15, 0),
                "break_end": datetime(1900, 1, 1, 18, 0),
                "shift_start": datetime(1900, 1, 1, 10, 0),
                "shift_end": datetime(1900, 1, 1, 23, 0)
        }


    def test_aling_breaks_2(self):
        assert self.parser.align_breaks_with_shift(example_2) == {
                "break_start": datetime(1900, 1, 1, 18, 30),
                "break_end": datetime(1900, 1, 1, 19, 0),
                "shift_start": datetime(1900, 1, 1, 18, 0),
                "shift_end": datetime(1900, 1, 1, 23, 0)
        }

    def test_aling_breaks_3(self):
        assert self.parser.align_breaks_with_shift(example_3) == {
                "break_start": datetime(1900, 1, 1, 16, 0),
                "break_end": datetime(1900, 1, 1, 17, 0),
                "shift_start": datetime(1900, 1, 1, 12, 0),
                "shift_end": datetime(1900, 1, 1, 22, 30)
        }
    def test_aling_breaks_4(self):
        assert self.parser.align_breaks_with_shift(example_4) == {
                "break_start": datetime(1900, 1, 1, 15, 0),
                "break_end": datetime(1900, 1, 1, 16, 0),
                "shift_start": datetime(1900, 1, 1, 9, 0),
                "shift_end": datetime(1900, 1, 1, 18, 0)
        }

    def test_aling_breaks_5(self):
        assert self.parser.align_breaks_with_shift(example_5) == {
                "break_start": datetime(1900, 1, 1, 16, 0),
                "break_end": datetime(1900, 1, 1, 16, 10),
                "shift_start": datetime(1900, 1, 1, 9, 0),
                "shift_end": datetime(1900, 1, 1, 23, 0)
        }

    def test_aling_breaks_6(self):
        assert self.parser.align_breaks_with_shift(example_6) == {
                "break_start": datetime(1900, 1, 1, 15, 0),
                "break_end": datetime(1900, 1, 1, 17, 0),
                "shift_start": datetime(1900, 1, 1, 11, 0),
                "shift_end": datetime(1900, 1, 1, 23, 0)
        }

    def test_aling_breaks_7(self):
        assert self.parser.align_breaks_with_shift(example_7) == {
            "break_start": datetime(1900, 1, 1, 11, 0),
            "break_end": datetime(1900, 1, 1, 13, 0),
            "shift_start": datetime(1900, 1, 1, 10, 0),
            "shift_end": datetime(1900, 1, 1, 16, 0)
            }

class TestExtractingPayRate:
    parser = ShiftParser()
    def test_extract_pay_rate_1(self):
        assert self.parser.extract_pay_rate(example_1) == 10.0

    def test_extract_pay_rate_2(self):
        assert self.parser.extract_pay_rate(example_2) == 12.0

    def test_extract_pay_rate_3(self):
        assert self.parser.extract_pay_rate(example_3) == 14.0

    def test_extract_pay_rate_4(self):
        assert self.parser.extract_pay_rate(example_4) == 10.0

    def test_extract_pay_rate_5(self):
        assert self.parser.extract_pay_rate(example_5) == 20.0

class TestExtractingShiftData:
    parser = ShiftParser()
    def test_extract_shift_data_1(self):
        assert self.parser.extract_shift_data(example_1) == {
                "break_start": datetime(1900, 1, 1, 15, 0),
                "break_end": datetime(1900, 1, 1, 18, 0),
                "shift_start": datetime(1900, 1, 1, 10, 0),
                "shift_end": datetime(1900, 1, 1, 23, 0),
                "pay_rate": 10.0
                }

    def test_extract_shift_data_2(self):
        assert self.parser.extract_shift_data(example_2) == {
                "break_start": datetime(1900, 1, 1, 18, 30),
                "break_end": datetime(1900, 1, 1, 19, 0),
                "shift_start": datetime(1900, 1, 1, 18, 0),
                "shift_end": datetime(1900, 1, 1, 23, 0),
                "pay_rate": 12.0
                }

class TestCalculatingLabourCosts:
    def test_calculate_single_labour_costs_1(self):
        parser = ShiftParser()
        assert parser.calculate_single_labour_costs(example_1) == {
        '10:00': 9.999999999999998,
        '11:00': 9.999999999999998,
        '12:00': 9.999999999999998,
        '13:00': 9.999999999999998,
        '14:00': 9.999999999999998,
        '18:00': 9.999999999999998,
        '19:00': 9.999999999999998,
        '20:00': 9.999999999999998,
        '21:00': 9.999999999999998,
        '22:00': 9.999999999999998
        }

    def test_calculate_single_labour_costs_1(self):
        parser = ShiftParser()
        assert parser.calculate_single_labour_costs(example_2) == {
        '18:00': 6.000000000000003,
        '19:00': 11.99999999999999,
        '20:00': 11.99999999999999,
        '21:00': 11.99999999999999,
        '22:00': 11.99999999999999,
        }

    def test_calculate_single_labour_costs_3(self):
        parser = ShiftParser()
        assert parser.calculate_single_labour_costs(example_3) == {
        '12:00': 13.99999999999998,
        '13:00': 13.99999999999998,
        '14:00': 13.99999999999998,
        '15:00': 13.99999999999998,
        '17:00': 13.99999999999998,
        '18:00': 13.99999999999998,
        '19:00': 13.99999999999998,
        '20:00': 13.99999999999998,
        '21:00': 13.99999999999998,
        '22:00': 7.000000000000001,
        }

    def test_calculate_single_labour_costs_4(self):
        parser = ShiftParser()
        assert parser.calculate_single_labour_costs(example_4) == {
        '09:00': 9.999999999999998,
        '10:00': 9.999999999999998,
        '11:00': 9.999999999999998,
        '12:00': 9.999999999999998,
        '13:00': 9.999999999999998,
        '14:00': 9.999999999999998,
        '16:00': 9.999999999999998,
        '17:00': 9.999999999999998,
        }

    def test_calculate_single_labour_costs_5(self):
        parser = ShiftParser()
        assert parser.calculate_single_labour_costs(example_5) == {
        '09:00': 19.999999999999996,
        '10:00': 19.999999999999996,
        '11:00': 19.999999999999996,
        '12:00': 19.999999999999996,
        '13:00': 19.999999999999996,
        '14:00': 19.999999999999996,
        '15:00': 19.999999999999996,
        '16:00': 16.666666666666675,
        '17:00': 19.999999999999996,
        '18:00': 19.999999999999996,
        '19:00': 19.999999999999996,
        '20:00': 19.999999999999996,
        '21:00': 19.999999999999996,
        '22:00': 19.999999999999996,
        }

    def test_calculate_single_labour_costs_6(self):
        parser = ShiftParser()
        assert parser.calculate_single_labour_costs(example_6) == {
        '11:00': 9.999999999999998,
        '12:00': 9.999999999999998,
        '13:00': 9.999999999999998,
        '14:00': 9.999999999999998,
        '17:00': 9.999999999999998,
        '18:00': 9.999999999999998,
        '19:00': 9.999999999999998,
        '20:00': 9.999999999999998,
        '21:00': 9.999999999999998,
        '22:00': 9.999999999999998,
        }

    def test_calculate_single_labour_costs_7(self):
        parser = ShiftParser()
        assert parser.calculate_single_labour_costs(example_7) == {
        '10:00': 9.999999999999998,
        '13:00': 9.999999999999998,
        '14:00': 9.999999999999998,
        '15:00': 9.999999999999998,
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
