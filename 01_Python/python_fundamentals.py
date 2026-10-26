# Python Fundamentals: Practice Examples

# 1. Variables and data types
name = "Machine Learning"
hours_studied = 3
completion_rate = 0.85

print(name, hours_studied, completion_rate)

# 2. Conditional statements
score = 82

if score >= 80:
    print("Strong performance")
else:
    print("More practice needed")

# 3. Functions
def calculate_average(values):
    if not values:
        return 0
    return sum(values) / len(values)


scores = [75, 82, 90, 88]
print("Average:", calculate_average(scores))

# 4. List comprehension
squared_numbers = [number ** 2 for number in range(1, 6)]
print("Squares:", squared_numbers)

# 5. Dictionary
topic_progress = {
    "Python": "Practiced",
    "NumPy": "Practiced",
    "Pandas": "Practiced",
    "Machine Learning": "In progress"
}

for topic, status in topic_progress.items():
    print(f"{topic}: {status}")
