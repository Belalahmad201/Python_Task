import time

# Brute Force Approach
def has_duplicate_bruteforce(ids):
    n = len(ids)
    for i in range(n):
        for j in range(i + 1, n):
            if ids[i] == ids[j]:
                return True
    return False


# Optimized Approach Using Set
def has_duplicate_set(ids):
    seen = set()

    for agent_id in ids:
        if agent_id in seen:
            return True
        seen.add(agent_id)

    return False


# Sample Data
agent_ids = [101, 205, 309, 404, 205]

# Brute Force Check
start = time.time()
result1 = has_duplicate_bruteforce(agent_ids)
end = time.time()

print("Brute Force Result:", result1)
print("Execution Time:", end - start, "seconds")


# Set-Based Check
start = time.time()
result2 = has_duplicate_set(agent_ids)
end = time.time()

print("\nSet-Based Result:", result2)
print("Execution Time:", end - start, "seconds")