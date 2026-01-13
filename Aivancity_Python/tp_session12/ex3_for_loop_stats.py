"""
Exercise 3: for loop + accumulation - statistics on N values
Goal: Use a for loop with range() and track totals.
"""

# Ask how many numbers user wants to enter
n = int(input("How many numbers do you want to enter? "))

# Initialize tracking variables
total = 0
min_value = None
max_value = None

# Loop through n iterations
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))
    total += number
    
    # Track minimum
    if min_value is None or number < min_value:
        min_value = number
    
    # Track maximum
    if max_value is None or number > max_value:
        max_value = number

# Calculate average
average = total / n

# Print statistics
print(f"Total sum: {total}")
print(f"Average: {average}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
