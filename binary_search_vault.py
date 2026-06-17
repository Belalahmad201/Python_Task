import time

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    step = 1

    print("\nBinary Search Visualization:")

    while left <= right:
        mid = (left + right) // 2

        print(f"Step {step}: left={left}, mid={mid}, right={right}, value={arr[mid]}")

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

        step += 1

    return -1


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Sorted vault of secret codes
vault = list(range(1, 100001))
target = 87654

# Binary Search Performance
start = time.time()
binary_result = binary_search(vault, target)
binary_time = time.time() - start

# Linear Search Performance
start = time.time()
linear_result = linear_search(vault, target)
linear_time = time.time() - start

print("\nResults")
print("-" * 30)
print(f"Target Found at Index: {binary_result}")
print(f"Binary Search Time : {binary_time:.8f} seconds")
print(f"Linear Search Time : {linear_time:.8f} seconds")

print("\nPerformance Difference:")
if binary_time < linear_time:
    print("Binary Search is faster because it halves the search space every step.")
else:
    print("Linear Search was faster in this run.")