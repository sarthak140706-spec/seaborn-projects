import matplotlib.pyplot as plt
import seaborn as sns
from data_inspection import data_inspection
from config import OUTPUT_DIR

def run_univariate_analysis(df):
    """
    Plot distributions of all numeric features (excluding target)
    and save plots to OUTPUT_DIR.
    """
    # Select numeric features, excluding target
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if 'Outcome' in numeric_features:
        numeric_features.remove('Outcome')
    
    for feature in numeric_features:
        plt.figure(figsize=(6,4))
        sns.histplot(df[feature], kde=True, bins=30, color='skyblue')
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')
        
        # Save plot
        plt.savefig(f'{OUTPUT_DIR}/univariate_{feature}.png', bbox_inches='tight')
        plt.close()
