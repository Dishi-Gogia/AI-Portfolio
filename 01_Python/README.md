# Python Fundamentals

## Overview

This module documents my Python learning as the foundation for data analysis, Machine Learning, and AI development.

It includes practical implementations of core programming concepts, reusable functions, data structures, and Python features used throughout the AI development workflow.

## Learning Objectives

- Understand Python syntax and fundamental programming concepts.
- Work with built-in data structures and collections.
- Write reusable functions and apply object-oriented programming principles.
- Use comprehensions, lambda expressions, and functional programming utilities.
- Build a foundation for NumPy, Pandas, and Machine Learning.
- Validate program behaviour using unit tests.

## Topics Covered

### 1. Python Fundamentals
- Variables and data types
- Strings, numbers, and Boolean values
- Conditional statements
- Loops and iteration
- Lists, tuples, sets, and dictionaries

### 2. Functions
- Defining and calling functions
- Parameters and return values
- Reusable logic
- Working with collections in functions
- Handling basic edge cases

### 3. Object-Oriented Programming
- Classes and objects
- Attributes and methods
- Core OOP concepts

### 4. Python Collections and Comprehensions
- List and dictionary comprehensions
- Iterating over collections
- Dictionary methods such as `items()`

### 5. Functional Programming Utilities
- Lambda expressions
- `map()`
- `filter()`
- `reduce()`

## Project Structure

```text
01_Python/
├── README.md
├── python_fundamentals.py
├── artifacts/
│   └── execution_output.txt
└── tests/
    ├── test_python_fundamentals.py
    └── output_artifacts.txt
```

*Note: `__pycache__/` directories are generated automatically by Python and are intentionally excluded from this documented structure.*

## Implementation

The `python_fundamentals.py` file contains practical examples of:

- Variables and data types
- Conditional statements
- Reusable functions
- List comprehensions
- Dictionaries and iteration
- Python programming fundamentals

## Running the Script

Run the following command from the repository root:

```bash
python 01_Python/python_fundamentals.py
```

The script output can be captured in `artifacts/execution_output.txt` for reference.

## Unit Testing

Unit tests are implemented using Python's built-in `unittest` framework.

The `tests/test_python_fundamentals.py` file validates selected functions and Python operations, including:

- Function return values
- Average calculation
- Empty-list handling
- List comprehension results
- Dictionary operations
- Basic edge cases

### Run the Unit Tests

Execute the following command from the repository root:

```bash
python -m unittest discover -s 01_Python/tests -v
```

The test runner reports the number of tests executed and whether they pass or fail.

### Test Output Artifact

The `tests/output_artifacts.txt` file is intended to store captured unit-test output for review and documentation.

## Artifacts and Results

The `artifacts/` directory contains execution evidence from the practical exercises.

- `artifacts/execution_output.txt` — terminal output from running the Python fundamentals script.
- `tests/output_artifacts.txt` — captured unit-test output, if maintained separately from the main execution artifact.

## Applications in AI and Machine Learning

Python is the core programming language used in this portfolio for:

- Data manipulation and analysis
- Numerical computing
- Machine Learning algorithms
- Data preprocessing and validation
- AI application development

## Tools and Technologies

- Python
- Visual Studio Code
- `unittest`
- Git and GitHub

## Repository Status

This module contains practical implementations of selected Python fundamentals and a unit-test suite for validating key operations.

Further exercises and test coverage will be added as the learning material progresses.

---

*Part of my AI and Machine Learning learning portfolio.*