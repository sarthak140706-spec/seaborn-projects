import os
import seaborn as sns

# Dataset path
DATASET_PATH = 'C:/Users/ASUS/OneDrive/Desktop/medical-data-visualization-seaborn/data/diabetes.csv'  # adjust filename/path as needed

# Output directory for plots
OUTPUT_DIR = 'plots'

# Visualization style
sns.set_style('whitegrid')  # global style for all plots

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
