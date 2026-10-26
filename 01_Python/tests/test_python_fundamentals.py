
import unittest
from pathlib import Path
import sys

# Allow the test to import the Python module from its parent folder.
PYTHON_FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PYTHON_FOLDER))

from python_fundamentals import calculate_average


class TestPythonFundamentals(unittest.TestCase):

    def test_calculate_average(self):
        """Average of multiple numbers should be calculated correctly."""
        self.assertEqual(calculate_average([75, 82, 90, 88]), 83.75)

    def test_calculate_average_single_value(self):
        """Average of a single value should equal that value."""
        self.assertEqual(calculate_average([10]), 10)

    def test_calculate_average_empty_list(self):
        """An empty list should return zero."""
        self.assertEqual(calculate_average([]), 0)

    def test_calculate_average_decimal_values(self):
        """Average should support decimal values."""
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.0]), 2.3333333333, places=8)

    def test_list_comprehension_example(self):
        """Squaring numbers should produce the expected values."""
        squared_numbers = [number ** 2 for number in range(1, 6)]
        self.assertEqual(squared_numbers, [1, 4, 9, 16, 25])

    def test_dictionary_iteration(self):
        """A dictionary should preserve the expected topic statuses."""
        topic_progress = {
            "Python": "Practiced",
            "NumPy": "Practiced",
            "Pandas": "Practiced",
            "Machine Learning": "In progress"
        }

        self.assertEqual(topic_progress["Python"], "Practiced")
        self.assertEqual(topic_progress["Machine Learning"], "In progress")


if __name__ == "__main__":
    unittest.main()