# Reverse String Program

text = input("Enter a string: ")

# Reverse the string
reversed_text = text[::-1]

print("Original String:", text)
print("Reversed String:", reversed_text)

# Analyze space usage
print("\nSpace Complexity: O(n)")
print("Because a new reversed string is created.")