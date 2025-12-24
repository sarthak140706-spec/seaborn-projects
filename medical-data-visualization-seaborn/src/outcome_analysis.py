import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config import OUTPUT_DIR
from data_inspection import data_inspection

def run_outcome_analysis(df):
    df_0 = df[df['Outcome'] == 0]
    df_1 = df[df['Outcome'] == 1]
    
    key_features = ['Glucose', 'BMI', 'Age', 'Insulin', 'BloodPressure']
    
    for feature in key_features:
        plt.figure(figsize=(6,4))
        sns.kdeplot(df_0[feature], label='Outcome 0', fill=True)
        sns.kdeplot(df_1[feature], label='Outcome 1', fill=True)
        plt.title(f'{feature} distribution by Outcome')
        plt.xlabel(feature)
        plt.ylabel('Density')
        plt.legend()
        plt.savefig(f'{OUTPUT_DIR}/outcome_{feature}.png', bbox_inches='tight')
        plt.close()
