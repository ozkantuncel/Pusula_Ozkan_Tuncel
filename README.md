# Pusula_Özkan_Tuncel

## Drug Side Analysis 

This application focuses on the analysis of reported side effects associated with drug usage. The data includes user information, drug start and end dates, drug names, side effects, and various other attributes. The analysis process primarily involves cleaning the data, filling in missing values, and visualizing the results.

## Getting Started

```bash
ilac_yan_etkileri_analizi/
│
├── data/
│   ├── raw/
│   │   └── ilac_yan_etkileri.xlsx
│   └── processed/
│       └── ilac_yan_etkileri_islenmiş.xlsx
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda.py
│   ├── preprocessor.py
│   └── visualizer.py
│
├── notebooks/
│   └── analiz.ipynb
│
├── reports/
│   └── eda_raporu.md
│
├── venv/
├── main.py
├── requirements.txt
└── README.md
```

The project includes the following key modules:

- `data_loader.py`: Handles loading data from various formats.
- `eda.py`: Performs basic exploratory data analysis.
- `preprocessor.py`: Handles data cleaning and preprocessing.
- `visualizer.py`: Visualizes the relationships in the data.
- `side_effect_analyzer.py`: Analyzes side effects in relation to drugs.

### Libraries Used

- [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
- [Seaborn](https://seaborn.pydata.org/): For statistical data visualization.
- [Matplotlib](https://matplotlib.org/): For plotting graphs and charts.
- [ydata-profiling](https://ydata-profiling.github.io/): For automated data profiling.
- [scikit-learn](https://scikit-learn.org/): For preprocessing and machine learning utilities.

### Setup

Before running the application, ensure you have Python 3.9+ and install the required packages:

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run the application with the following command:

```bash
$ python main.py
```

## Modules Overview

### Data Loader

The `DataLoader` class is responsible for loading the data from different file formats such as `.csv` and `.xlsx`.

- **`load_data()`**: Loads the data based on file extension.
- **`check_data_format()`**: Prints the file format for verification.

### Exploratory Data Analysis (EDA)

The `EDA` class performs initial data analysis tasks such as:

- **`basic_info()`**: Displays general information about the dataset.
- **`data_profile()`**: Generates a detailed profiling report.
- **`missing_values()`**: Identifies missing values and their percentages.

### Preprocessor

The `Preprocessor` class handles preprocessing steps such as:

- **`fill_missing_values()`**: Fills missing values using various strategies.
- **`encode_categorical()`**: Encodes categorical features into numerical values.
- **`scale_features()`**: Standardizes or normalizes numerical features.

### Side Effect Analyzer

The `SideEffectAnalyzer` class analyzes side effects related to drugs:

- **`most_common_side_effects()`**: Identifies the most frequently reported side effects.
- **`drug_side_effect_relationship()`**: Displays drug and side effect relationships.
- **`analyze_effect_of_chronic_conditions()`**: Analyzes how chronic conditions affect side effects.

### Visualizer

The `Visualizer` class handles the visualization of key insights:

- **`plot_missing_data()`**: Plots a heatmap of missing data.
- **`plot_class_distribution()`**: Displays the distribution of categorical variables.
- **`plot_correlation_matrix()`**: Visualizes correlations between numerical features.

```
MIT License

Copyright (c) 2024 Özkan TUNCEL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
