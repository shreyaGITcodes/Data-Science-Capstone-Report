# DATA3888 Data Science Capstone - Group Report
**Stock Volatility Prediction Using Machine Learning**  
**Group 21 - Optiver Stream**

## 📚 Report Overview

This repository contains the comprehensive report and supporting materials for our DATA3888 Data Science Capstone project. We investigate and compare various machine learning approaches for predicting stock market volatility using high-frequency trading data provided by Optiver.

### 📑 Main Report
The complete project report is available at: [`docs/DATA3888_Group_Report.html`](docs/DATA3888_Group_Report.html)

## 🎯 Project Summary

Our project explores the challenge of predicting realized volatility in financial markets, a critical metric for risk management and trading strategies. We implement and evaluate multiple approaches:

- **Traditional Time Series Models**: LAG and HAR-RV models as baselines
- **Machine Learning Approaches**: Linear Regression, Random Forest, and Gradient Boosting
- **Deep Learning**: Graph Attention Networks (GAT) to capture inter-stock relationships
- **Dimensionality Reduction**: PCA-enhanced models for improved performance

### Key Findings
- PCA-Linear model achieved the best overall performance (RMSE: 0.917)
- GAT models showed promise in capturing complex market dynamics
- Feature engineering significantly improved prediction accuracy

## 📊 Repository Structure

```
├── docs/                           # Report and documentation
│   ├── DATA3888_Group_Report.html  # Main project report (view this!)
│   ├── DATA3888_Group_Report.qmd   # Quarto source file
│   └── DATA3888_Group_Report_files/# Report assets
│
├── figures/                        # Figures and visualizations used in report
│
├── notebooks/                      # Analysis notebooks
│   ├── baseline_training.ipynb     # Model training procedures
│   └── Baseline_evaluation.ipynb   # Model evaluation and comparison
│
├── results/                        # Model outputs and performance metrics
│   ├── model_metrics_summary.csv   # Comparative performance table
│   └── *_predictions.csv           # Individual model predictions
│
├── models/                         # Trained model files
│   └── best_gat_model.pt          # Best performing GAT model
│
└── data/                          # Data files (see .gitignore for excluded files)
    ├── raw/                       # Original Optiver datasets
    └── processed/                 # Processed features and targets
```

## 📈 Model Performance Summary

| Model | RMSE | QLIKE | RMPSE | MAPE |
|-------|------|-------|-------|------|
| **PCA_Linear** | **0.917** | **8.804** | 4.24e9 | 3.40e17 |
| LAG | 0.942 | 8.850 | 4.63e9 | 3.96e17 |
| Random_Forest | 0.956 | 8.832 | 4.42e9 | 3.70e17 |
| Linear | 0.967 | 8.844 | 4.53e9 | 3.88e17 |
| HAR_RV | 0.978 | 8.851 | 4.53e9 | 3.85e17 |
| Gradient_Boosting | 1.043 | 8.848 | 4.52e9 | 4.08e17 |

## 🚀 Key Deliverables

1. **Comprehensive Report**: Detailed analysis of volatility prediction methods
2. **Shiny Web Application**: Interactive tool for stock volatility analysis (VoltaTrade)
3. **Model Implementations**: Reproducible code for all approaches
4. **Performance Analysis**: Thorough evaluation using multiple metrics

## 💡 Project Highlights

- **Interdisciplinary Approach**: Combines finance, machine learning, and software engineering
- **Real-world Application**: Addresses actual trading challenges faced by Optiver
- **Novel Methods**: Explores Graph Attention Networks for financial time series
- **Practical Impact**: Developed tools useful for investors and traders

## 🛠️ Technical Stack

- **Languages**: Python, R (for report generation)
- **ML Libraries**: scikit-learn, PyTorch, pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Web Framework**: Python Shiny
- **Report Generation**: Quarto

## 👥 Team Members

Group 21:
- Shreya Prakash (520496062)
- Chenuka Garunsinghe (530080640)
- Binh Minh Tran (530414672)
- Enoch Wong (530531430)
- Ruohai Tao (540222281)
- Zoha Kausar (530526838)

## 📝 Viewing the Report

To view the main report:
1. Clone this repository
2. Open `docs/Report_group_21.html` in your web browser

For the interactive Shiny application:
- Deployed at: [https://binhminhtran-volatility-explorer.share.connect.posit.cloud/]
- Source code: [https://github.com/idolbinhminhtran/Volatility-Explorer]


## 🙏 Acknowledgments

- **Optiver** for providing the real-world dataset and problem statement
- **DATA3888 Course Team** for guidance and support
- **University of Sydney** for the learning opportunity

---

*For questions about this project, please contact the team members or raise an issue in this repository.*
