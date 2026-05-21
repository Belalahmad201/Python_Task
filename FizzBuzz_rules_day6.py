# FizzBuzz Automation

n = int(input("Enter a number: "))

# Open file in write mode
file = open("fizzbuzz_output.txt", "w")

for i in range(1, n + 1):

    if i % 3 == 0 and i % 5 == 0:
        result = "FizzBuzz"

    elif i % 3 == 0:
        result = "Fizz"

    elif i % 5 == 0:
        result = "Buzz"

    else:
        result = str(i)

    print(result)
    file.write(result + "\n")

file.close()

print("Output saved in fizzbuzz_output.txt")