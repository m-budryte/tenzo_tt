from datetime import datetime, timedelta
from parsers.full_string_parser import *
"""
Please write you name here: Masha Budryte
"""


def process_shifts(path_to_csv):
    string = open(path_to_csv).read()

    return {}

# def process_sales(path_to_csv):
#     return
#
# def compute_percentage(shifts, sales):
#     return
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