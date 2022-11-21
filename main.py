#!/usr/bin/env python
"""6G-assessment

In this file you will find all the things you need to run for the 6G-assessment.
"""

from datetime import datetime
from calendar import monthrange
import pandas as pd
import numpy as np


def load_data(PATH: str):
    """
    Use Pandas' read_csv function to read out a csv into a pd.DataFrame

    :param PATH: Path to input file
    :return: DataFrame
    """
    return pd.read_csv(PATH)


#
def clean_data(df: pd.DataFrame):
    """
    In the data we observe a string "4,5" that should be converted to a float value of 4.5

    :param df: DataFrame
    :return: DataFrame with cleaned up/consistent data
    """
    # Make sure we also drop all NaN's
    df.dropna()

    df['Workdays per week'] = df['Workdays per week'].apply(lambda dist: conv_comma_to_dot(dist))
    return df


def conv_comma_to_dot(val: str):
    """
    Replace any strings that contain commas to dots, also convert them to float values

    :param val: String value that might need correction
    :return: A float value where the comma/dot has been corrected
    """
    if type(val) == str:
        conv_val = float(val.replace(",", "."))
        return conv_val
    else:
        return val


def add_calculated_compensation(df: pd.DataFrame):
    """
    Apply the calculation to the original DataFrame

    :param df: DataFrame
    :return: DataFrame with added column
    """
    df[f'Compensation for {datetime.now().strftime("%B")}'] = df.apply(lambda x: compensation_calculator(x['Transport'],
                                                                                                         x['Distance (km/one way)'],
                                                                                                         x['Workdays per week']), axis=1)

    return df


def compensation_calculator(transport: str, distance: int, workdays: int):
    """
    Calculate the compensation for employee

    :param transport: Mode of transport that an Employee uses
    :param distance: Distance that the Employee has to travel
    :param workdays: Amount of workdays per week that an Employee has
    :return: Compensation that an Employee gets for the month
    """
    # Calculate compensation for one day of work.
    if transport == "Bike":
        if 5 <= distance:
            day_comp = 1 * distance
        else:
            day_comp = 0.5 * distance

    elif transport in ["Bus", "Train"]:
        day_comp = 0.25 * distance
    else:
        day_comp = 0.1 * distance

    amount_workdays = calc_amount_workdays(workdays)

    return amount_workdays * day_comp


def calc_amount_workdays(workdays: int):
    """
    Calculate the amount of workdays an employee works in month

    :param workdays: Amount of workdays per week that an Employee has
    :return: Amount of workdays in the month
    """
    # Date now, date can be altered to test future/past dates.
    now = datetime.today()
    # now = Your Date Here -> also change in line 92 and 93

    # Get the date of first day of the month
    first_date = now.replace(day=1)
    # Get the amount of days in the month
    days_in_month = monthrange(first_date.year, first_date.month)[1]
    # Get the date of last day of the month
    last_date = now.replace(day=days_in_month)
    # Get which weekday the last day of the month is
    last_weekday = last_date.isoweekday()
    # Get which weekday the first day of the month is
    first_weekday = first_date.isoweekday()

    workday_count = 4 * workdays
    weekday_count = first_weekday - 1
    while weekday_count < last_weekday and weekday_count < workdays:
        workday_count += 1
        weekday_count += 1

    return workday_count


def add_pay_date(df: pd.DataFrame):
    """
    Apply payment date to DataFrame

    :param df: DataFrame
    :return: DataFrame with added column
    """
    df['Payment date'] = find_first_monday()
    return df


def find_first_monday():
    """
    Find the first monday of next month

    :return: String with the date of the first monday of the next month
    """
    # Find the next month
    year = datetime.now().year
    month = datetime.now().month

    if month == 12:  # If it's the last month of the year
        month = 1
        year += 1
    else:
        month += 1

    # Correctly converts month to string by pasting a zero in front
    if month < 10:
        month = str(month).zfill(2)

    return str(np.busday_offset(f"{year}-{month}", 0,
                                roll='forward',
                                weekmask='Mon'))


def export_data(df: pd.DataFrame, PATH: str):
    """
    Export the data to a .csv file

    :param df: DataFrame
    :param PATH: Path to export folder
    :return: None
    """
    df.to_csv(PATH)
    print(f"Succesfully saved to {PATH}")


def main():
    df = load_data("data/employee_data.csv")
    df = clean_data(df)
    df = add_calculated_compensation(df)
    df = add_pay_date(df)
    export_data(df, "data/employee_data_compensation.csv")


if __name__ == '__main__':
    main()
