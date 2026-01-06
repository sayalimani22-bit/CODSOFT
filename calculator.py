# Simple Calculator in Python

def calculator():
    # Prompt user for inputs
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform the calculation based on operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return
        
        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")

# Run the calculator
calculator()