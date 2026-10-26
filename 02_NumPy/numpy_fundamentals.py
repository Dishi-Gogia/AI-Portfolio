
import numpy as np

# 1. Array creation
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)

# 2. Reshaping
matrix = np.arange(1, 7).reshape(2, 3)
print("\nMatrix:\n", matrix)
print("Transpose:\n", matrix.T)

# 3. Filtering and conditional selection
values = np.array([12, 25, 8, 40, 18])
print("\nValues greater than 15:", values[values > 15])
print("Classified values:", np.where(values >= 20, "High", "Low"))

# 4. Statistical operations
print("\nMean:", np.mean(values))
print("Median:", np.median(values))
print("Standard deviation:", np.std(values))
print("Minimum index:", np.argmin(values))
print("Maximum index:", np.argmax(values))

# 5. Unique values and counting
categories = np.array([1, 2, 2, 3, 3, 3])
print("\nUnique values:", np.unique(categories, return_counts=True))

# 6. Normalization (Min-Max)
minimum = values.min()
maximum = values.max()

normalized = (values - minimum) / (maximum - minimum)
print("\nNormalized values:", normalized)

# 7. Reproducible random numbers
np.random.seed(42)
random_values = np.random.randint(1, 100, size=5)
print("\nRandom values:", random_values)

