"""
Exercise 2: Conditionals - simple decision system
Goal: Practice if/elif/else and readable conditions.
"""

# First decision: positive, negative, or zero
num1 = float(input("Enter a number: "))

if num1 > 0:
    print("positive")
elif num1 < 0:
    print("negative")
else:
    print("zero")

# Second decision: compare two numbers
num2 = float(input("Enter a second number: "))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num1 < num2:
    print(f"{num2} is larger than {num1}")
else:
    print(f"{num1} and {num2} are equal")
