# Addition function
def add(x, y):
    return x + y

# Subtraction function
def sub(x, y):
    return x - y

# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def division(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

# Function to display the menu and handle user input
def display_menu():
    print("\n+ : add")
    print("- : subtract")
    print("* : multiply")
    print("/ : divide")
    print("n : input new numbers")
    print("enter : exit program")

def main():
    result = None  # Initialize result variable to None

    while True:
        if result is None:
            try:
                x = float(input("Enter a number: "))
                y = float(input("Enter a second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue
        else:
            use_prev = input(f"Do you want to use the previous result ({result})? (y/n): ").lower()
            if use_prev == 'y':
                x = result
                y = float(input("Enter a second number: "))
            else:
                try:
                    x = float(input("Enter a number: "))
                    y = float(input("Enter a second number: "))
                except ValueError:
                    print("Please enter valid numbers.")
                    continue

        display_menu()

        choice = input("Enter your choice: ")
        if choice == '+':
            result = add(x, y)
            print(f"Result: {result}")
        elif choice == '-':
            result = sub(x, y)
            print(f"Result: {result}")
        elif choice == '*':
            result = multiply(x, y)
            print(f"Result: {result}")
        elif choice == '/':
            result = division(x, y)
            print(f"Result: {result}")
        elif choice == 'n':
            result = None  # Reset result to allow input of new numbers
            continue
        elif choice == '':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
