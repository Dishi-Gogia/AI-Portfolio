import sys
import unittest
from pathlib import Path

# Make the parent project folder available for imports
PROJECT_FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_FOLDER))

from data_quality_practice import (
    create_employee_dataset,
    create_cleaning_copy,
    handle_missing_salary,
    find_repeated_employee_ids,
    remove_exact_duplicates,
)


class TestDataQualityPractice(unittest.TestCase):

    def setUp(self):
        """Create a fresh dataset for each test."""
        self.original_df = create_employee_dataset()

    def test_dataset_has_seven_rows(self):
        self.assertEqual(len(self.original_df), 7)

    def test_dataset_has_one_missing_salary(self):
        missing_count = self.original_df["Salary"].isnull().sum()
        self.assertEqual(missing_count, 1)

    def test_missing_salary_is_filled_with_median(self):
        cleaned_df = handle_missing_salary(self.original_df)

        self.assertEqual(
            cleaned_df["Salary"].isnull().sum(),
            0
        )

        self.assertEqual(
            cleaned_df.loc[
                cleaned_df["EmployeeID"] == "E102", "Salary"
            ].iloc[0],
            85000
        )

    def test_original_data_remains_unchanged(self):
        handle_missing_salary(self.original_df)

        self.assertEqual(
            self.original_df["Salary"].isnull().sum(),
            1
        )

    def test_repeated_employee_id_detection(self):
        repeated_records = find_repeated_employee_ids(
            self.original_df
        )

        self.assertEqual(len(repeated_records), 2)
        self.assertTrue(
            (repeated_records["EmployeeID"] == "E105").all()
        )

    def test_exact_duplicate_removal(self):
        cleaned_df = remove_exact_duplicates(self.original_df)

        self.assertEqual(len(cleaned_df), 6)
        self.assertEqual(cleaned_df.duplicated().sum(), 0)

    def test_duplicate_removal_preserves_original(self):
        remove_exact_duplicates(self.original_df)

        self.assertEqual(len(self.original_df), 7)
        self.assertEqual(self.original_df.duplicated().sum(), 1)


if __name__ == "__main__":
    unittest.main()
    