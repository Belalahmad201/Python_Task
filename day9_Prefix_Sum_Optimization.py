# Prefix Sum Optimization Example

# Original array
arr = [2, 4, 1, 6, 3, 5]

# Create prefix sum array
prefix = [0] * len(arr)

# First element remains same
prefix[0] = arr[0]

# Build prefix sum array
for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("Original Array:", arr)
print("Prefix Sum Array:", prefix)

# Function to answer range sum query
def range_sum(left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]

# Multiple queries
queries = [(0, 2), (1, 4), (2, 5)]

print("\nRange Sum Queries:")

for l, r in queries:
    print(f"Sum from index {l} to {r} =", range_sum(l, r))