class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def getMin(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]

    def display(self):
        print("Stack:", self.stack)
        print("Current Min:", self.getMin())


# Testing with random inputs
vault = MinStack()

temperatures = [34, 29, 41, 22, 30, 18, 25]

print("Adding temperature readings...")
for temp in temperatures:
    vault.push(temp)
    print(f"Pushed {temp}, Min = {vault.getMin()}")

print("\nRemoving readings...")
while vault.stack:
    removed = vault.pop()
    print(f"Popped {removed}, New Min = {vault.getMin()}")