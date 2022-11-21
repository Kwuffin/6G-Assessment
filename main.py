from datetime import datetime
from calendar import monthrange
import pandas as pd
import numpy as np


# Use Pandas' read_csv function to read out a csv into a pd.DataFrame
def load_data(PATH: str):
    return pd.read_csv(PATH)


# In the data we observe a string "4,5" that should be converted to a float value of 4.5
def clean_data(df: pd.DataFrame):
    # Make sure we also drop all NaN's
    df.dropna()

    df['Workdays per week'] = df['Workdays per week'].apply(lambda dist: conv_comma_to_dot(dist))
    return df


# Replace any strings that contain commas to dots, also convert them to float values
def conv_comma_to_dot(val: str):
    if type(val) == str:
        conv_val = float(val.replace(",", "."))
        return conv_val
    else:
        return val


# Apply the calculation to the original DataFrame
def add_calculated_compensation(df: pd.DataFrame):
    df['Compensation'] = df.apply(lambda x: compensation_calculator(x['Transport'],
                                                                    x['Distance (km/one way)'],
                                                                    x['Workdays per week']), axis=1)

    return df


# Calculate the compensation for employee
def compensation_calculator(transport, distance, workdays):
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


# Calculate the amount of workdays an employee works in month
def calc_amount_workdays(workdays):
    # Date now, date can be altered to test future/past dates.
    now = datetime.today()

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


def main():
    df = load_data("data/employee_data.csv")
    df = clean_data(df)
    df = add_calculated_compensation(df)
    df =
    print(df)


if __name__ == '__main__':
    main()
