"""
Exercise 1: Environment + first CLI interaction (I/O + types)
Goal: Confirm environment is correct and practice basic input/output.
"""

current_year = 2026

# Ask for user input
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
birth_year = input("What is your birth year? ")

# Convert birth year to int and compute age
birth_year = int(birth_year)
age = current_year - birth_year

# Print formatted message with f-string
print(f"Hello {first_name} {last_name}, you are approximately {age} years old.")
