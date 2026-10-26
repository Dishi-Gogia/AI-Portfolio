import pandas as pd

# 1. Create a DataFrame
data = {
    "Employee": ["Asha", "Ravi", "Meera", "Kabir", "Neha"],
    "Department": ["QA", "Data", "QA", "ML", "Data"],
    "Experience": [5, 3, 8, 2, 6],
    "Salary": [80000, 65000, 95000, 55000, 85000]
}

df = pd.DataFrame(data)

# 2. Inspect the data
print("First rows:\n", df.head())
print("\nShape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nSummary:\n", df.describe())

# 3. Filter rows
experienced = df.loc[df["Experience"] >= 5]
print("\nExperience >= 5:\n", experienced)

# 4. Create a derived column
df["Experience_Level"] = df["Experience"].apply(
    lambda years: "Senior" if years >= 5 else "Junior"
)

# 5. Group and aggregate
department_summary = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Employee_Count=("Employee", "count")
)
print("\nDepartment summary:\n", department_summary)

# 6. Handle missing values
df.loc[1, "Salary"] = None
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print("\nAfter filling missing salary:\n", df)

# 7. Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())

# 8. Encode categories
encoded = pd.get_dummies(df["Department"], dtype=int)
print("\nEncoded departments:\n", encoded)