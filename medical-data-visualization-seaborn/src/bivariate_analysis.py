import matplotlib.pyplot as plt
import seaborn as sns
from config import OUTPUT_DIR
from data_inspection import data_inspection

def run_bivariate_analysis(df):
    """
    Plot scatterplots for selected feature pairs colored by Outcome.
    """
    # Example feature pairs
    feature_pairs = [
        ('Glucose', 'BMI'),
        ('Age', 'BloodPressure'),
        ('Insulin', 'SkinThickness')
    ]
    
    for x_feat, y_feat in feature_pairs:
        plt.figure(figsize=(6,4))
        sns.scatterplot(
            data=df,
            x=x_feat,
            y=y_feat,
            hue='Outcome',
            palette='Set1'
        )
        plt.title(f'{y_feat} vs {x_feat} by Outcome')
        plt.savefig(f'{OUTPUT_DIR}/bivariate_{x_feat}_{y_feat}.png', bbox_inches='tight')
        plt.close()
