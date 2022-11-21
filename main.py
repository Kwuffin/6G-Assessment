import pandas as pd
import numpy as np

# This function uses Pandas' read_csv function to read out a csv into a pd.DataFrame
def load_data(PATH):
    return pd.read_csv(PATH)


# In the data we observe a string "4,5" that should be converted to a float value of 4.5
def clean_data(df: pd.DataFrame):
    # Make sure we also drop all NaN's
    df.dropna()

    df['Workdays per week'] = df['Workdays per week'].apply(lambda dist: conv_comma_to_dot(dist))
    print(df.to_string())
    return df


# This function replaces any commas in strings to dots
def conv_comma_to_dot(val: str):
    if type(val) == str:
        conv_val = float(val.replace(",", "."))
        return conv_val
    else:
        return val


def main():
    df = load_data("data/employee_data.csv")
    clean_data(df)


if __name__ == '__main__':
    main()
