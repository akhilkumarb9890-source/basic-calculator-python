import math

def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")  # new feature

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice!")
        return

    if choice == "5":
        num = float(input("Enter number: "))
        print("Result:", math.sqrt(num))
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

calculator()
# This is for push feature checking 