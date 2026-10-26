# NumPy Fundamentals

## Overview

This module documents my hands-on learning of NumPy, a Python library for numerical computing. It covers array manipulation, mathematical operations, statistical analysis, and numerical transformations used in data analysis and Machine Learning.

The examples are implemented using Python scripts in Visual Studio Code, with unit tests to validate selected numerical operations.

## Learning Objectives

- Create and manipulate NumPy arrays efficiently.
- Understand array dimensions, shapes, indexing, and reshaping.
- Perform vectorized calculations and conditional selection.
- Apply statistical operations to numerical data.
- Understand normalization and reproducible random number generation.
- Validate numerical operations using unit tests.

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

## Project Structure

```text
02_NumPy/
├── README.md
├── numpy_fundamentals.py
├── artifacts/
│   └── execution_output.txt
└── tests/
    ├── test_numpy_fundamentals.py
    └── output_artifacts.txt
```

*Note: `__pycache__/` directories are generated automatically by Python and are not included in this documented structure.*

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

Execute this command from the repository root:

```bash
python 02_NumPy/numpy_fundamentals.py
```

## Unit Testing

Unit tests are implemented using Python's built-in `unittest` framework.

The `tests/test_numpy_fundamentals.py` file contains tests for the following scenarios:

- Array shape and dimensions
- Matrix reshaping
- Matrix transposition
- Filtering values
- Mean and median calculations
- Minimum and maximum indices
- Min-Max normalization
- Unique values and their counts

### Run the Unit Tests

From the repository root, execute:

```bash
python -m unittest discover -s 02_NumPy/tests -v
```

The test runner displays each test's result and reports the total number of tests executed.

### Test Output Artifact

The file `tests/output_artifacts.txt` can store captured unit-test output for review and documentation.

## Artifacts and Results

The `artifacts/` directory stores execution evidence from practical exercises.

- `artifacts/execution_output.txt` — terminal output demonstrating array operations, filtering, statistical calculations, normalization, and random number generation.
- `tests/output_artifacts.txt` — captured unit-test output, if maintained separately.

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
- `unittest`
- Git and GitHub

## Repository Status

This module contains practical implementations of selected NumPy concepts and a unit-test suite for validating key numerical operations.

Additional exercises and test coverage will be added as the learning material progresses.

---

*Part of my AI and Machine Learning learning portfolio.*