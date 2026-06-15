from collections import Counter

def topKFrequent(nums, k):
    frequency = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in frequency.items():
        buckets[freq].append(num)

    result = []

    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))