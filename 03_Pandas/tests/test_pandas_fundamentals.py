
import unittest
import pandas as pd


def create_sample_dataframe():
    """Create a predictable DataFrame for testing."""
    return pd.DataFrame({
        "Employee": ["Asha", "Ravi", "Meera", "Kabir", "Neha"],
        "Department": ["QA", "Data", "QA", "ML", "Data"],
        "Experience": [5, 3, 8, 2, 6],
        "Salary": [80000, 65000, 95000, 55000, 85000]
    })


class TestPandasFundamentals(unittest.TestCase):

    def setUp(self):
        self.df = create_sample_dataframe()

    def test_dataframe_shape(self):
        self.assertEqual(self.df.shape, (5, 4))

    def test_select_column(self):
        salaries = self.df["Salary"]

        self.assertEqual(len(salaries), 5)
        self.assertEqual(salaries.iloc[0], 80000)

    def test_filter_experienced_employees(self):
        experienced = self.df.loc[
            self.df["Experience"] >= 5
        ]

        self.assertEqual(len(experienced), 3)
        self.assertEqual(
            experienced["Employee"].tolist(),
            ["Asha", "Meera", "Neha"]
        )

    def test_derived_experience_level(self):
        self.df["Experience_Level"] = self.df["Experience"].apply(
            lambda years: "Senior" if years >= 5 else "Junior"
        )

        self.assertEqual(
            self.df["Experience_Level"].tolist(),
            ["Senior", "Junior", "Senior", "Junior", "Senior"]
        )

    def test_groupby_aggregation(self):
        summary = self.df.groupby("Department").agg(
            Average_Salary=("Salary", "mean"),
            Employee_Count=("Employee", "count")
        )

        self.assertEqual(summary.loc["QA", "Average_Salary"], 87500)
        self.assertEqual(summary.loc["QA", "Employee_Count"], 2)
        self.assertEqual(summary.loc["Data", "Employee_Count"], 2)

    def test_fill_missing_values(self):
        self.df.loc[1, "Salary"] = None

        median_salary = self.df["Salary"].median()
        self.df["Salary"] = self.df["Salary"].fillna(median_salary)

        self.assertFalse(self.df["Salary"].isnull().any())
        self.assertEqual(self.df.loc[1, "Salary"], 82500)

    def test_duplicate_detection(self):
        duplicated_df = pd.concat(
            [self.df, self.df.iloc[[0]]],
            ignore_index=True
        )

        self.assertEqual(duplicated_df.duplicated().sum(), 1)

    def test_one_hot_encoding(self):
        encoded = pd.get_dummies(
            self.df["Department"],
            dtype=int
        )

        self.assertEqual(set(encoded.columns), {"Data", "ML", "QA"})
        self.assertEqual(encoded.shape, (5, 3))
        self.assertEqual(encoded["QA"].sum(), 2)


if __name__ == "__main__":
    unittest.main()
