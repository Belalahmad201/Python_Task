# Day 8 - Arrays in Python

# Create an array (list) of numbers
numbers = [12, 345, 2, 7896, 44, 1001, 6789, 55, 8, 2222]

# Variable to count numbers with even digits
even_digit_count = 0

# Check each number
for num in numbers:
    digit_count = len(str(num))  # Count digits

    # Check if digit count is even
    if digit_count % 2 == 0:
        even_digit_count += 1

# Print results
print("Array Elements:", numbers)
print("Numbers with even number of digits:", even_digit_count)

# Short explanation
print("\nExplanation:")
print("Arrays are used in real systems to store and manage large amounts of data efficiently.")
print("Examples include user activity logs, analytics dashboards, banking systems, and social media feeds.")