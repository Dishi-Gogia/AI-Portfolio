# Pandas Fundamentals and Data Analysis

## Overview

This module documents my hands-on learning of Pandas, a Python library for data manipulation and analysis. It covers DataFrame operations, data inspection, filtering, aggregation, missing-value handling, and feature transformation techniques relevant to Machine Learning.

The examples are implemented using Python scripts in Visual Studio Code, with unit tests to validate selected data manipulation and preprocessing operations.

## Learning Objectives

- Load, inspect, and understand structured datasets.
- Select, filter, and transform rows and columns.
- Summarize data using grouping and aggregation.
- Identify and handle missing and duplicate records.
- Apply functions and transform categorical features.
- Prepare structured datasets for Machine Learning workflows.
- Validate data manipulation operations using unit tests.

## Topics Covered

### 1. DataFrame Creation and Inspection

- Creating DataFrames using `pd.DataFrame()`
- Inspecting data with `head()`, `tail()`, `shape`, and `columns`
- Understanding data types using `dtypes` and `info()`
- Generating statistical summaries using `describe()`

### 2. Data Selection and Filtering

- Selecting columns
- Filtering rows using conditions
- Selecting data with `loc` and `iloc`
- Filtering using `isin()` and `between()`

### 3. Data Transformation

- Creating derived columns
- Renaming columns
- Replacing and mapping values
- Applying functions using `apply()` and lambda expressions
- Working with categorical data using `get_dummies()`

### 4. Grouping and Aggregation

- Grouping records using `groupby()`
- Calculating aggregates using `agg()`
- Summarizing data across categories

### 5. Data Quality

- Identifying missing values using `isnull()` and `isna()`
- Handling missing values with `fillna()` and `dropna()`
- Detecting duplicates using `duplicated()`
- Removing duplicate records using `drop_duplicates()`

### 6. Dates and Numerical Analysis

- Working with dates using `pd.Timestamp`
- Calculating tenure from date columns
- Applying statistical summaries and numerical transformations

## Project Structure

```text
03_Pandas/
├── README.md
├── pandas_fundamentals.py
├── artifacts/
│   └── execution_output.txt
└── tests/
    ├── test_pandas_fundamentals.py
    └── output_artifacts.txt
```

*Note: `__pycache__/` directories are generated automatically by Python and are not included in this documented structure.*

## Implementation

The file `pandas_fundamentals.py` demonstrates:

- DataFrame creation and inspection
- Row filtering using conditional expressions
- Derived columns and experience classification
- Department-level grouping and aggregation
- Missing-value handling
- Duplicate detection
- One-hot encoding of categorical variables

### Run the Script

Execute this command from the repository root:

```bash
python 03_Pandas/pandas_fundamentals.py
```

## Unit Testing

Unit tests are implemented using Python's built-in `unittest` framework.

The `tests/test_pandas_fundamentals.py` file covers the following scenarios:

- DataFrame shape validation
- Column selection
- Filtering employees by experience
- Derived columns and experience classification
- GroupBy aggregation
- Missing-value imputation using the median
- Duplicate detection
- One-hot encoding

### Run the Unit Tests

From the repository root, execute:

```bash
python -m unittest discover -s 03_Pandas/tests -v
```

**Latest recorded result:** All 8 unit tests passed.

These tests validate selected Pandas operations used in data analysis and data preprocessing workflows.

### Test Output Artifact

The file `tests/output_artifacts.txt` can store captured unit-test output for review and documentation.

## Artifacts and Results

The `artifacts/` directory stores execution evidence from the practical exercises.

- `artifacts/execution_output.txt` — terminal output from running the Pandas fundamentals script.
- `tests/output_artifacts.txt` — captured unit-test output, if maintained separately.

## Applications in Machine Learning

Pandas supports Machine Learning workflows by helping with:

- Understanding raw datasets
- Detecting data quality issues
- Selecting relevant features
- Transforming categorical and numerical data
- Preparing structured data for model training and evaluation

## Tools and Technologies

- Python
- Pandas
- NumPy
- Visual Studio Code
- `unittest`
- Git and GitHub

## Repository Status

This module contains practical implementations of selected Pandas concepts and a unit-test suite for validating key operations.

Further exercises and test coverage will be added as the learning material progresses.

---

*Part of my AI and Machine Learning learning portfolio.*