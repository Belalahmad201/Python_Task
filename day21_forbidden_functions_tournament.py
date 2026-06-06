# Day 21 - The Forbidden Functions Tournament

# Problem 1: Recursion - Factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
print("Factorial of", number, "=", factorial(number))


print("\n" + "=" * 40 + "\n")


# Problem 2: Stack - Reverse String

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()


text = "ENGINEER"

stack = Stack()

for ch in text:
    stack.push(ch)

reversed_text = ""

while len(stack.items) > 0:
    reversed_text += stack.pop()

print("Original String :", text)
print("Reversed String :", reversed_text)


print("\nReflection:")
print("Today I solved one recursion problem and one stack problem.")
print("I avoided helper functions such as sort(), sum(), max(), and min().")
print("This challenge helped me understand low-level problem solving and")
print("how recursion and stacks work internally.")