"""
Exercise 5: Mini menu program (integration of Sessions 1–2)
Goal: Combine I/O + conversions + conditionals + loops into a small CLI tool.
"""


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


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


def read_menu_choice() -> int:
    """
    Display menu and get valid user choice (1, 2, or 3).
    
    Returns:
        The valid menu choice (1, 2, or 3)
    """
    while True:
        print("\n=== Conversion Menu ===")
        print("1. Celsius to Fahrenheit")
        print("2. Kilometers to Miles")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Main program loop."""
    while True:
        choice = read_menu_choice()
        
        if choice == 1:
            celsius = read_float("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        
        elif choice == 2:
            km = read_float("Enter distance in kilometers: ")
            miles = km_to_miles(km)
            print(f"{km} km = {miles:.2f} miles")
        
        elif choice == 3:
            print("Thank you! Goodbye!")
            break


if __name__ == "__main__":
    main()
