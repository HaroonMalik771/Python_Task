import math

def addition():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("Result: ", result)

def subtraction():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("Result: ", result)

def multiplication():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("Result: ", result)

def division():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Cannot divide by zero.")

def trig_operations():
    while True:
        print("\nTrigonometric Operations:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Go back to the main menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            angle = float(input("Enter the angle in degrees: "))
            result = math.sin(math.radians(angle))
            print("Result: ", result)
        elif choice == 2:
            angle = float(input("Enter the angle in degrees: "))
            result = math.cos(math.radians(angle))
            print("Result: ", result)
        elif choice == 3:
            angle = float(input("Enter the angle in degrees: "))
            result = math.tan(math.radians(angle))
            print("Result: ", result)
        elif choice == 4:
            return
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Arithmetic Operations")
        print("2. Trigonometric Operations")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            arithmetic_menu()
        elif choice == 2:
            trig_operations()
        elif choice == 3:
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice.")

def arithmetic_menu():
    while True:
        print("\nArithmetic Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Go back to the main menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            return
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
