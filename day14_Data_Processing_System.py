# Mini Data Processing System

# Dataset (Student Scores)
scores = [85, 90, 78, 92, 85, 78, 95, 88, 90, 85]

# Hashing using Dictionary
frequency = {}

for score in scores:
    if score in frequency:
        frequency[score] += 1
    else:
        frequency[score] = 1

# Generate Insights
total_students = len(scores)
average_score = sum(scores) / total_students
highest_score = max(scores)
lowest_score = min(scores)

print("=== Mini Data Processing System ===")
print("Total Students:", total_students)
print("Average Score:", round(average_score, 2))
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)

print("\nScore Frequency:")
for score, count in frequency.items():
    print(f"Score {score}: {count} student(s)")