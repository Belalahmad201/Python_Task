# Day 16/60 🚀 | ABTalks Coding Challenge

## 🎯 The Task
The Infinite Staircase Puzzle

A robot is climbing a staircase and can take either **1 step** or **2 steps** at a time.

The goal is to calculate the total number of different ways the robot can reach step **N**.

---

## 💻 What I Worked On

- Implemented a recursive solution
- Understood recursive problem-solving
- Optimized the solution using memoization
- Compared recursive and optimized approaches
- Analyzed time complexity and space complexity

---

## 🧠 Solution Approach

To reach step **N**, the robot can:

1. Reach step **N-1** and take 1 step
2. Reach step **N-2** and take 2 steps

Therefore:

```python
f(n) = f(n-1) + f(n-2)
```

This follows the Fibonacci sequence pattern.

---

## 📝 Recursive Solution

```python
def climb_stairs(n):
    if n <= 1:
        return 1

    return climb_stairs(n - 1) + climb_stairs(n - 2)

n = 5
print("Number of ways =", climb_stairs(n))
```

### Output

```text
Number of ways = 8
```

---

## ⚡ Optimized Solution (Memoization)

```python
def climb_stairs_memo(n, memo={}):
    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)

    return memo[n]

n = 5
print("Number of ways =", climb_stairs_memo(n))
```

### Output

```text
Number of ways = 8
```

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Recursion | O(2ⁿ) | O(n) |
| Memoization | O(n) | O(n) |

---

## 🌳 Recursion Tree (N = 4)

```text
climb(4)
├── climb(3)
│   ├── climb(2)
│   │   ├── climb(1)
│   │   └── climb(0)
│   └── climb(1)
└── climb(2)
    ├── climb(1)
    └── climb(0)
```

Memoization avoids recalculating repeated subproblems and improves performance significantly.

---

## 🧠 Key Learnings

- Recursion breaks complex problems into smaller subproblems.
- Recursive solutions may perform redundant calculations.
- Memoization stores computed results for reuse.
- Dynamic Programming improves efficiency.
- Similar techniques are used in AI search systems, pathfinding algorithms, and game engines.

---

## 🔗 GitHub Repository

Add your repository link here:

```text
https://github.com/Belalahmad201/Python_Task
```

---

### Day 16 Complete ✅