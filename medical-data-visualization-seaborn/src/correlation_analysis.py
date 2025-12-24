import matplotlib.pyplot as plt
import seaborn as sns
from config import OUTPUT_DIR
from data_inspection import data_inspection

def run_correlation_analysis(df):
    """
    Compute correlation matrix of numeric features (excluding target)
    and save heatmap.
    """
    # Select numeric features excluding Outcome
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if 'Outcome' in numeric_features:
        numeric_features.remove('Outcome')

    # Compute correlation
    corr_matrix = df[numeric_features].corr()

    # Plot heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap of Numeric Features')
    plt.savefig(f'{OUTPUT_DIR}/correlation_heatmap.png', bbox_inches='tight')
    plt.close()
