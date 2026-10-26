# NumPy Fundamentals

## Overview

This module documents my hands-on learning of NumPy, a Python library for numerical computing. It covers array manipulation, mathematical operations, statistical analysis, and numerical transformations used in data analysis and Machine Learning.

## Learning Objectives

- Create and manipulate NumPy arrays efficiently.
- Understand array dimensions, shapes, indexing, and reshaping.
- Perform vectorized calculations and conditional selection.
- Apply statistical operations to numerical data.
- Understand normalization and reproducible random number generation.

## Topics Covered

### 1. Array Creation and Structure
- Creating arrays using `np.array()`, `np.arange()`, `np.zeros()`, `np.ones()`, and `np.full()`
- Understanding `shape`, `ndim`, and data types
- Reshaping arrays using `reshape()` and `flatten()`

### 2. Array Manipulation
- Transposing arrays using `.T`
- Concatenation and stacking: `concatenate()`, `vstack()`, `hstack()`, and `stack()`
- Splitting, inserting, and deleting array elements

### 3. Searching and Sorting
- Sorting arrays using `sort()` and `argsort()`
- Finding minimum and maximum indices using `argmin()` and `argmax()`
- Counting non-zero values using `count_nonzero()`
- Conditional selection using `np.where()`
- Identifying unique values using `np.unique()`

### 4. Statistical Operations
- Mean and median
- Standard deviation and variance
- Percentiles and interquartile range (IQR)
- Applying statistical operations to numerical arrays

### 5. Numerical Transformations
- Min-Max normalization
- Standardization
- Array-based mathematical operations

### 6. Random Number Generation
- Generating random values
- Using `np.random.seed()` for reproducibility

## Implementation

The file `numpy_fundamentals.py` contains practical examples of:

- Array creation and inspection
- Reshaping and transposition
- Filtering and conditional selection
- Statistical calculations
- Unique values and frequency counts
- Min-Max normalization
- Reproducible random number generation

### Run the Script

```bash
python 02_NumPy/numpy_fundamentals.py
```

Run this command from the repository root. If NumPy is installed and the file is in the expected location, the script prints the results to the terminal.

## Artifacts and Results

The `artifacts/` directory preserves execution evidence from the practical exercises.

Planned artifact:

- `artifacts/execution_output.txt` — terminal output showing array shapes, matrix transposition, filtering, statistical calculations, normalization, and reproducible random values.

These artifacts provide evidence of successful execution and make the learning exercises easier to review.

## Applications in Machine Learning

NumPy provides foundational numerical operations for Machine Learning, including:

- Representing numerical features as arrays and matrices
- Performing vectorized calculations
- Understanding matrix dimensions and transformations
- Computing descriptive statistics
- Applying numerical scaling and normalization

## Tools and Technologies

- Python
- NumPy
- Visual Studio Code
- Git and GitHub

## Repository Status

This module contains practical implementations of selected NumPy concepts. Additional exercises and execution artifacts will be added as the learning material is reviewed and organized.

---

*Part of my AI and Machine Learning learning portfolio.*
