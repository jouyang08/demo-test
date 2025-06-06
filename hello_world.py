import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def square(a):
    return a * a

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Cannot calculate square root of a negative number."

def main():
    print("Welcome to the Calculator Program!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        if choice in ['5', '6']:
            if choice == '5':
                num1 = float(input("Enter a number to square: "))
                print(f"The result is: {square(num1)}")
            elif choice == '6':
                num1 = float(input("Enter a number to find square root: "))
                print(f"The result is: {square_root(num1)}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input. Please restart the program.")

if __name__ == "__main__":
    main()