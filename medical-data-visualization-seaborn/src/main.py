from data_loader import getData
from data_inspection import data_inspection
from univariate_analysis import run_univariate_analysis
from outcome_analysis import run_outcome_analysis
from bivariate_analysis import run_bivariate_analysis
from correlation_analysis import run_correlation_analysis

def main():
    print("Starting program...\n")
    
    # Load dataset
    df = getData()
    
    # Inspect dataset
    df, target = data_inspection()
    
    # Run analyses
    run_univariate_analysis(df)
    run_outcome_analysis(df)
    run_bivariate_analysis(df)
    run_correlation_analysis(df)
    
    print("\nProgram finished.")

if __name__ == "__main__":
    main()
