from datetime import datetime, timedelta
from parsers.work_shifts_parser import *
from parsers.transactions_parser import *
"""
Please write you name here: Masha Budryte
"""


def process_shifts(path_to_csv):
    string = open(path_to_csv).read()
    return calculate_total_labour_cost(string)

def process_sales(path_to_csv):
    string = open(path_to_csv).read()
    return calculate_profits(string)

def compute_percentage(shifts, sales):
    percentage_income = {}
    percentage_income.update(sales)
    print(percentage_income)
    for hour in shifts:
        percentage_income[hour] = -shifts[hour]
    print(percentage_income)
    return percentage_income
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
