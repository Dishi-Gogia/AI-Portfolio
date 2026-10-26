
import unittest
import numpy as np


class TestNumPyFundamentals(unittest.TestCase):

    def test_array_shape_and_dimensions(self):
        arr = np.array([10, 20, 30, 40, 50])

        self.assertEqual(arr.shape, (5,))
        self.assertEqual(arr.ndim, 1)

    def test_matrix_reshape(self):
        matrix = np.arange(1, 7).reshape(2, 3)

        self.assertEqual(matrix.shape, (2, 3))
        np.testing.assert_array_equal(
            matrix,
            np.array([[1, 2, 3], [4, 5, 6]])
        )

    def test_matrix_transpose(self):
        matrix = np.arange(1, 7).reshape(2, 3)

        expected = np.array([
            [1, 4],
            [2, 5],
            [3, 6]
        ])

        np.testing.assert_array_equal(matrix.T, expected)

    def test_filter_values(self):
        values = np.array([12, 25, 8, 40, 18])

        actual = values[values > 15]
        expected = np.array([25, 40, 18])

        np.testing.assert_array_equal(actual, expected)

    def test_mean_and_median(self):
        values = np.array([12, 25, 8, 40, 18])

        self.assertAlmostEqual(np.mean(values), 20.6)
        self.assertAlmostEqual(np.median(values), 18.0)

    def test_minimum_and_maximum_indices(self):
        values = np.array([12, 25, 8, 40, 18])

        self.assertEqual(np.argmin(values), 2)
        self.assertEqual(np.argmax(values), 3)

    def test_min_max_normalization(self):
        values = np.array([12, 25, 8, 40, 18])

        normalized = (
            (values - values.min()) /
            (values.max() - values.min())
        )

        self.assertAlmostEqual(normalized.min(), 0.0)
        self.assertAlmostEqual(normalized.max(), 1.0)

        np.testing.assert_allclose(
            normalized,
            np.array([0.125, 0.53125, 0.0, 1.0, 0.3125])
        )

    def test_unique_values_and_counts(self):
        values = np.array([1, 2, 2, 3, 3, 3])

        unique_values, counts = np.unique(
            values,
            return_counts=True
        )

        np.testing.assert_array_equal(unique_values, [1, 2, 3])
        np.testing.assert_array_equal(counts, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()