def generate_combinations(gems):
    result = []

    def backtrack(start, current):
        # Current subset ko result me add karo
        result.append(current[:])

        # Remaining gems ko try karo
        for i in range(start, len(gems)):
            current.append(gems[i])      # Choose
            backtrack(i + 1, current)    # Explore
            current.pop()                # Backtrack

    backtrack(0, [])
    return result


# Input
gems = ["Ruby", "Emerald", "Diamond"]

# Generate all combinations
combinations = generate_combinations(gems)

# Output
print("All Gem Combinations:")
for combo in combinations:
    print(combo)

print("\nTotal Combinations:", len(combinations))