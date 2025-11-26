# Smart Calculator by Hassan

def hassan_calculator():
    print("=== Smart Calculator ===")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)

        if b != 0:
            print("Division:", a / b)
        else:
            print("Division: Error! Cannot divide by zero.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

