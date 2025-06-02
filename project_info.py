#!/usr/bin/env python3
"""
Project Information Script
Provides information about the DATA3888 Capstone Report repository structure
"""

import os
from pathlib import Path

def print_project_structure():
    """Print the project directory structure"""
    print("\n📁 REPORT REPOSITORY STRUCTURE:")
    print("=" * 50)
    
    structure = {
        "docs/": {
            "DATA3888_Group_Report.html": "Main project report (VIEW THIS!)",
            "DATA3888_Group_Report.qmd": "Quarto source file",
            "DATA3888_Group_Report_files/": "Report assets and dependencies"
        },
        "figures/": "Figures and visualizations used in the report",
        "notebooks/": {
            "baseline_training.ipynb": "Model training procedures",
            "Baseline_evaluation.ipynb": "Model evaluation and comparison"
        },
        "results/": {
            "model_metrics_summary.csv": "Performance comparison table",
            "*_predictions.csv": "Individual model prediction outputs"
        },
        "models/": "Trained model files (e.g., best_gat_model.pt)",
        "data/": {
            "raw/": "Original Optiver datasets (see .gitignore)",
            "processed/": "Processed features and targets"
        }
    }
    
    for main_dir, contents in structure.items():
        print(f"\n{main_dir}")
        if isinstance(contents, dict):
            for item, desc in contents.items():
                print(f"  └── {item} - {desc}")
        else:
            print(f"  └── {contents}")

def check_report_files():
    """Check report-related files"""
    print("\n📝 REPORT FILES STATUS:")
    print("=" * 50)
    
    # Check main report
    report_path = Path("docs/DATA3888_Group_Report.html")
    if report_path.exists():
        size_mb = report_path.stat().st_size / (1024 * 1024)
        print(f"\n✓ Main report available: {size_mb:.1f} MB")
        print(f"  Open docs/DATA3888_Group_Report.html in your browser to view")
    else:
        print("\n✗ Main report not found in docs/")
    
    # Check figures directory
    figures_path = Path("figures")
    if figures_path.exists():
        figures = list(figures_path.glob("*"))
        if figures:
            print(f"\n✓ Figures directory: {len(figures)} files")
        else:
            print("\n⚠ Figures directory exists but is empty")
    else:
        print("\n⚠ Figures directory not found")

def check_results():
    """Check available results"""
    print("\n📊 MODEL RESULTS STATUS:")
    print("=" * 50)
    
    results_path = Path("results")
    if results_path.exists():
        # Check metrics summary
        metrics_file = results_path / "model_metrics_summary.csv"
        if metrics_file.exists():
            print("\n✓ Model performance summary available")
            print("  Best model: PCA_Linear (RMSE: 0.917)")
        
        # Check predictions
        prediction_files = list(results_path.glob("*_predictions.csv"))
        if prediction_files:
            print(f"\n✓ Model predictions: {len(prediction_files)} models")
            for f in sorted(prediction_files):
                model_name = f.stem.replace("_predictions", "")
                print(f"  - {model_name}")

def print_key_findings():
    """Print key findings from the project"""
    print("\n🎯 KEY FINDINGS:")
    print("=" * 50)
    print("\n1. PCA-Linear model achieved best performance (RMSE: 0.917)")
    print("2. Feature engineering significantly improved predictions")
    print("3. GAT models captured complex inter-stock relationships")
    print("4. Traditional HAR-RV model provided strong baseline")

def main():
    """Main function to display project information"""
    print("\n📚 DATA3888 CAPSTONE PROJECT REPORT")
    print("Stock Volatility Prediction Using Machine Learning")
    print("Group 21 - Optiver Stream")
    print("=" * 50)
    
    print_project_structure()
    check_report_files()
    check_results()
    print_key_findings()
    
    print("\n\n📖 HOW TO VIEW THE REPORT:")
    print("=" * 50)
    print("1. Open docs/DATA3888_Group_Report.html in your web browser")
    print("2. Or navigate to the docs/ folder and double-click the HTML file")
    
    print("\n💻 ADDITIONAL RESOURCES:")
    print("=" * 50)
    print("- Notebooks: Check notebooks/ for detailed analysis")
    print("- Results: See results/ for all model outputs")
    print("- Figures: Browse figures/ for visualizations")
    
    print("\n✨ For more information, check the README.md file!")

if __name__ == "__main__":
    main() 