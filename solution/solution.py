from datetime import datetime, timedelta
from parsers.shift_parser import ShiftParser
from parsers.transaction_parser import TransactionParser
"""
Please write you name here: Masha Budryte
"""


def process_shifts(path_to_csv):
    string = open(path_to_csv).read()
    parser = ShiftParser()
    return parser.total_labour_cost(string)

def process_sales(path_to_csv):
    string = open(path_to_csv).read()
    parser = TransactionParser()
    return parser.calculate_profit(string)

# def compute_percentage(shifts, sales):

#
# def best_and_worst_hour(percentages):
#     return

def main(path_to_shifts, path_to_sales):
    """
    Do not touch this function, but you can look at it, to have an idea of
    how your data should interact with each other
    """

    shifts_processed = process_shifts(path_to_shifts)
    sales_processed = process_sales(path_to_sales)
    percentages = compute_percentage(shifts_processed, sales_processed)
    best_hour, worst_hour = best_and_worst_hour(percentages)
    return best_hour, worst_hour

if __name__ == '__main__':
    # You can change this to test your code, it will not be used
    path_to_sales = 'transactions.csv'
    path_to_shifts = 'work_shifts.csv'
    best_hour, worst_hour = main(path_to_shifts, path_to_sales)


# Please write you name here: Masha Budryte
