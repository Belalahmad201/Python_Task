# Week 5 Sprint Challenge

## Problem 1: Longest Consecutive Sequence

### Approach
- Store elements in a HashSet.
- Start counting only from sequence beginnings.
- Expand sequence until consecutive numbers stop.

### Complexity
- Time: O(n)
- Space: O(n)

### Tradeoff
Extra memory is used for faster lookup operations.

---

## Problem 2: Top K Frequent Elements

### Approach
- Count frequencies using Counter.
- Use Bucket Sort to group numbers by frequency.
- Traverse buckets from highest frequency.

### Complexity
- Time: O(n)
- Space: O(n)

### Tradeoff
Consumes extra memory but avoids O(n log n) sorting.

---

## Why These Solutions Scale

Both solutions achieve O(n) time complexity, making them suitable for large datasets commonly encountered in engineering interviews and production systems.