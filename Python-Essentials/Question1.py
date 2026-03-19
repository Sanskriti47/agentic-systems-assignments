try:
    # Take input from user
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    # Check if the second number is 0
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        # Print Sum
        print("Sum:", num1+num2)
        # Print division
        print("Division:", num1/num2)
except ValueError:
    print("Invalid input")

