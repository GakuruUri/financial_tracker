import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])