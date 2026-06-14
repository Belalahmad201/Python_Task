from collections import Counter
import heapq

# Sample hashtag stream
hashtags = [
    "#AI", "#Python", "#AI", "#DataScience",
    "#Python", "#AI", "#Coding", "#Python",
    "#MachineLearning", "#AI", "#Coding"
]

k = 3

# Frequency Analysis
frequency = Counter(hashtags)

print("Hashtag Frequencies:")
for tag, count in frequency.items():
    print(f"{tag}: {count}")

# Top K Frequent Hashtags using Heap
top_k = heapq.nlargest(k, frequency.items(), key=lambda x: x[1])

print("\nTop", k, "Trending Hashtags:")
for tag, count in top_k:
    print(f"{tag} -> {count}")