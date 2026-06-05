class RPNCalculator:

    def evaluate(self, tokens):
        stack = []

        for token in tokens:

            if token in ['+', '-', '*', '/']:

                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)

                elif token == '-':
                    stack.append(a - b)

                elif token == '*':
                    stack.append(a * b)

                elif token == '/':
                    stack.append(int(a / b))   # truncate toward zero

            else:
                stack.append(int(token))

        return stack[-1]


# Test Cases
calculator = RPNCalculator()

print(calculator.evaluate(["2", "1", "+", "3", "*"]))      # 9
print(calculator.evaluate(["4", "13", "5", "/", "+"]))     # 6
print(calculator.evaluate(["10", "6", "9", "3", "+", "-11",
                           "*", "/", "*", "17", "+", "5", "+"]))  # 22