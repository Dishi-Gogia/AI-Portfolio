# Pandas Fundamentals and Data Analysis

## Overview

This module documents my hands-on learning of Pandas, a Python library for data manipulation and analysis. It covers DataFrame operations, data inspection, filtering, aggregation, missing-value handling, and feature transformation techniques relevant to Machine Learning.

## Learning Objectives

- Load, inspect, and understand structured datasets.
- Select, filter, and transform rows and columns.
- Summarize data using grouping and aggregation.
- Identify and handle missing and duplicate records.
- Apply functions and transform categorical features.
- Prepare structured datasets for Machine Learning workflows.

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

## Implementation

The file `pandas_fundamentals.py` demonstrates:

- DataFrame creation and inspection
- Row filtering using conditional expressions
- Derived columns using lambda functions
- Department-level grouping and aggregation
- Missing-value handling
- Duplicate detection
- One-hot encoding of categorical variables

### Run the Script

```bash
python 03_Pandas/pandas_fundamentals.py
```

Run this command from the repository root.

## Artifacts and Results

The `artifacts/` directory preserves execution evidence from the practical exercises.

Planned artifact:

- `artifacts/execution_output.txt` — terminal output showing DataFrame inspection, filtered records, derived columns, group-level summaries, missing-value handling, duplicate checks, and categorical encoding.

These artifacts help demonstrate the implementation and results of the exercises.

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
- Git and GitHub

## Repository Status

This module contains practical implementations of selected Pandas concepts. Additional exercises, notebooks, and execution artifacts will be added as the learning material is reviewed and organized.

---

*Part of my AI and Machine Learning learning portfolio.*