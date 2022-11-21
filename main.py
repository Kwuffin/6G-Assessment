import pandas as pd
import numpy as np


def load_data(PATH):
    return pd.read_csv(PATH)


def main():
    load_data("data/employee_data.csv")


if __name__ == '__main__':
    main()
