import pandas as pd


def create_employee_dataset():
    """Create a sample employee dataset with intentional data-quality issues."""

    data = {
        "EmployeeID": [
            "E101", "E102", "E103", "E104",
            "E105", "E105", "E106"
        ],
        "Department": [
            "QA", "Data", "QA", "data",
            "QA", "QA", "Data"
        ],
        "ExperienceYears": [5, 3, 8, -2, 6, 6, 10],
        "Salary": [80000, None, 95000, 55000, 85000, 85000, 500000],
        "PerformanceScore": [4, 3, 5, 2, 4, 4, 5]
    }

    return pd.DataFrame(data)


def assess_data_quality(df):
    """Report potential data-quality issues without modifying the dataset."""

    print("=" * 55)
    print("EMPLOYEE DATA QUALITY ASSESSMENT")
    print("=" * 55)

    print("\n1. Dataset overview")
    print("-" * 30)
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print(f"Column names: {list(df.columns)}")

    print("\n2. Data types")
    print("-" * 30)
    print(df.dtypes)

    print("\n3. Missing values by column")
    print("-" * 30)
    print(df.isnull().sum())

    print("\n4. Duplicate rows")
    print("-" * 30)
    print(f"Exact duplicate rows: {df.duplicated().sum()}")

    print("\n5. Duplicate employee IDs")
    print("-" * 30)
    print(f"Repeated employee IDs: {df['EmployeeID'].duplicated().sum()}")

    print("\n6. Invalid experience values")
    print("-" * 30)
    invalid_experience = df[df["ExperienceYears"] < 0]
    print(invalid_experience)

    print("\n7. Potential salary outliers")
    print("-" * 30)
    q1 = df["Salary"].quantile(0.25)
    q3 = df["Salary"].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    potential_outliers = df[
        (df["Salary"] < lower_bound)
        | (df["Salary"] > upper_bound)
    ]

    print(f"Lower IQR bound: {lower_bound:.2f}")
    print(f"Upper IQR bound: {upper_bound:.2f}")
    print(potential_outliers)

    print("\n8. Department category inconsistencies")
    print("-" * 30)
    print("Department values:")
    print(df["Department"].value_counts(dropna=False))

    print("\n9. Numerical summary")
    print("-" * 30)
    print(df[["ExperienceYears", "Salary", "PerformanceScore"]].describe())

    print("\nAssessment complete. Original data remains unchanged.")

def investigate_missing_values(df):
    """Return missing-value counts for each column."""
    missing_counts = df.isnull().sum()

    print("\nMissing-value investigation:")
    print(missing_counts)

    return missing_counts

def investigate_duplicates(df):
    """Identify exact duplicate rows and repeated employee IDs."""
    exact_duplicates = df[df.duplicated()]

    repeated_ids = df[
        df["EmployeeID"].duplicated(keep=False)
    ].sort_values("EmployeeID")

    print("\nExact duplicate rows:")
    print(exact_duplicates)

    print("\nRecords with repeated employee IDs:")
    print(repeated_ids)

    return exact_duplicates, repeated_ids

def create_cleaning_copy(df):
    """Create a separate copy so the original data remains unchanged."""
    return df.copy()

def handle_missing_salary(df):
    """Fill missing salaries with the median of observed salaries."""

    cleaned_df = df.copy()

    missing_before = cleaned_df["Salary"].isnull().sum()
    median_salary = cleaned_df["Salary"].median()

    cleaned_df["Salary"] = cleaned_df["Salary"].fillna(
        median_salary
    )

    missing_after = cleaned_df["Salary"].isnull().sum()

    print("\nMissing Salary Handling")
    print("-" * 30)
    print(f"Missing salaries before: {missing_before}")
    print(f"Median salary used: {median_salary}")
    print(f"Missing salaries after: {missing_after}")

    return cleaned_df

def find_repeated_employee_ids(df):
    """Return all rows with repeated employee IDs for investigation."""

    repeated_records = df[
        df["EmployeeID"].duplicated(keep=False)
    ].sort_values("EmployeeID")

    print("\nRepeated employee ID investigation")
    print("-" * 35)

    if repeated_records.empty:
        print("No repeated employee IDs found.")
    else:
        print(repeated_records)

    return repeated_records

def remove_exact_duplicates(df):
    """Remove exact duplicate rows without modifying the input DataFrame."""

    cleaned_df = df.copy()

    rows_before = len(cleaned_df)
    duplicates_before = cleaned_df.duplicated().sum()

    cleaned_df = cleaned_df.drop_duplicates()

    rows_removed = rows_before - len(cleaned_df)
    duplicates_after = cleaned_df.duplicated().sum()

    print("\nExact duplicate handling")
    print("-" * 30)
    print(f"Duplicate rows detected: {duplicates_before}")
    print(f"Duplicate rows removed: {rows_removed}")
    print(f"Duplicate rows remaining: {duplicates_after}")
    print(f"Rows remaining: {len(cleaned_df)}")

    return cleaned_df

def detect_iqr_outliers(df, column):
    """Identify potential outliers using the IQR method."""

    values = df[column].dropna()

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[
        (df[column] < lower_bound)
        | (df[column] > upper_bound)
    ]

    print(f"\nIQR Outlier Investigation: {column}")
    print("-" * 40)
    print(f"Q1: {q1:.2f}")
    print(f"Q3: {q3:.2f}")
    print(f"IQR: {iqr:.2f}")
    print(f"Lower bound: {lower_bound:.2f}")
    print(f"Upper bound: {upper_bound:.2f}")
    print(f"Potential outliers detected: {len(outliers)}")
    print(outliers)

    return outliers

if __name__ == "__main__":
    employee_df = create_employee_dataset()
   # assess_data_quality(employee_df)
    # Keep the original dataset unchanged
    working_df = create_cleaning_copy(employee_df)

    investigate_missing_values(working_df)
    investigate_duplicates(working_df)

    cleaned_df = handle_missing_salary(working_df)

    print("\nCleaned salary column:")
    print(cleaned_df[["EmployeeID", "Salary"]])

    print("\nOriginal salary column remains unchanged:")
    print(employee_df[["EmployeeID", "Salary"]])

    salary_outliers = detect_iqr_outliers(
    employee_df,
    "Salary"
    )