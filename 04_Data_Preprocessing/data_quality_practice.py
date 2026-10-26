import pandas as pd

# 1. Create a dataset with deliberate quality issues
data = {
    "Employee_ID": [101, 102, 103, 103, 105, 106],
    "Experience": [2, 5, None, None, 8, 120],
    "Salary": [50000, 75000, 60000, 60000, None, 90000],
    "Department": ["QA", "Data", "ML", "ML", "Unknown", "QA"]
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df)

# 2. Inspect the dataset
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate employee IDs:")
print(df["Employee_ID"].duplicated().sum())

# 3. Validate data types and ranges
print("\nInvalid experience values:")
print(df.loc[
    (df["Experience"] < 0) | (df["Experience"] > 50)
])

allowed_departments = {"QA", "Data", "ML"}

print("\nInvalid departments:")
print(df.loc[~df["Department"].isin(allowed_departments)])

# 4. Remove exact duplicate rows
df_clean = df.drop_duplicates().copy()

# 5. Handle missing values
df_clean["Experience"] = df_clean["Experience"].fillna(
    df_clean["Experience"].median()
)

df_clean["Salary"] = df_clean["Salary"].fillna(
    df_clean["Salary"].median()
)

# 6. Validate the cleaned dataset
print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())

print("\nCleaned dataset:")
print(df_clean)

print("\nRows remaining:", len(df_clean))
