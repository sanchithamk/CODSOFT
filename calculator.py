def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")

    try:
        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Get user input for operation
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter the number of the operation (1/2/3/4): ")

        # Perform the calculation based on the user's choice
        if operation == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
