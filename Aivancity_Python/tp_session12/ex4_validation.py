"""
Exercise 4: while loop + validation - robust input reader
Goal: Build a reusable validation pattern.
"""


def read_float(prompt: str) -> float:
    """
    Repeatedly ask user for a float until valid input is provided.
    
    Args:
        prompt: The message to display to the user
        
    Returns:
        The valid float entered by the user
    """
    while True:
        user_input = input(prompt).strip()
        
        try:
            value = float(user_input)
            return value
        except ValueError:
            print(f"Invalid input: '{user_input}'. Please enter a valid number.")


# Main program
if __name__ == "__main__":
    num1 = read_float("Enter the first number: ")
    num2 = read_float("Enter the second number: ")
    
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}")
