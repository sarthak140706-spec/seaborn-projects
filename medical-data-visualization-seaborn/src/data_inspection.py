import pandas as pd
from data_loader import getData

def data_inspection():
    df = getData()
    print("---------------------------------------------------------")
    print("First 5 rows:")
    print(df.head(5))
    print("---------------------------------------------------------")
    print("Columns:", list(df.columns))
    print("---------------------------------------------------------")
    print("Shape of dataset:", df.shape)
    print("---------------------------------------------------------")
    print("Missing values in each column:")
    print(df.isnull().sum())
    print("---------------------------------------------------------")
    target = df['Outcome']
    print("Target column 'Outcome' identified with", target.shape[0], "rows")

    return df,target
data_inspection()