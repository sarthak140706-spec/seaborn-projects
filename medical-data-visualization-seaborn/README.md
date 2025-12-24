# Medical Data Visualization using Seaborn

This project performs exploratory data analysis (EDA) and visualization on a medical dataset (diabetes dataset). It includes univariate, outcome-based, bivariate, and correlation analyses using Python, Pandas, Matplotlib, and Seaborn.

## Project Structure

medical-data-visualization-seaborn/
│
├─ src/
│ ├─ main.py # Main script to run all analyses
│ ├─ config.py # Configuration for dataset path and output directory
│ ├─ data_loader.py # Loads the dataset
│ ├─ data_inspection.py # Inspects dataset, identifies target
│ ├─ univariate_analysis.py # Plots distribution of numeric features
│ ├─ outcome_analysis.py # Compares features across Outcome groups
│ ├─ bivariate_analysis.py # Plots relationships between feature pairs
│ ├─ correlation_analysis.py # Computes correlation matrix and heatmap
│ └─ utils.py # Helper functions for plotting
│
├─ data/ # Dataset folder
│ └─ diabetes.csv
│
└─ plots/ # Folder where all plots are saved

bash
Copy code

## How to Run

1. Clone the repository and navigate to the `src` folder:

```bash
git clone <repo-url>
cd medical-data-visualization-seaborn/src
Make sure the dataset is in data/diabetes.csv.

Run the main script:

bash
Copy code
python main.py
All plots will be saved automatically in the plots/ folder.

Features
Univariate Analysis: Distribution of numeric features.

Outcome Analysis: Compare distributions of features for Outcome=0 vs Outcome=1.

Bivariate Analysis: Scatterplots of selected feature pairs colored by Outcome.

Correlation Analysis: Heatmap of numeric feature correlations.