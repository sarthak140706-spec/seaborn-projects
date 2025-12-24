import pandas as pd

def getData():
    df = pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/medical-data-visualization-seaborn/data/diabetes.csv")
    print("Data loaded successfully...")
    return df 