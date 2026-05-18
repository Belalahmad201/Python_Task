# Taking list input
numbers = input("Enter numbers separated by space: ")

# Convert input into list
numbers_list = list(map(int, numbers.split()))

# Sum
total = sum(numbers_list)

# Max
maximum = max(numbers_list)

# Min
minimum = min(numbers_list)

# Frequency count using dictionary
frequency = {}

for num in numbers_list:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Reverse list without built-in function
reversed_list = []

for i in range(len(numbers_list) - 1, -1, -1):
    reversed_list.append(numbers_list[i])

# Output
print("Sum:", total)
print("Max:", maximum)
print("Min:", minimum)
print("Frequency:", frequency)
print("Reversed List:", reversed_list)