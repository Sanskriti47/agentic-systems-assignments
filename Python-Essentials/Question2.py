try:
    # take first name and last name
    first_name = input("Enter your First name:")
    last_name = input("Enter your Last name:")
    # take age and convert it to integer 
    age = int(input("Enter your current age:"))
    # check if age is negative 
    if age < 0:
        print("Age cannot be negative")
    else:
        # print full name using concatenation
        full_name = first_name + " " + last_name
        print("Full name:", full_name)
    # Age next year 
        print("You will be", age+1, "next year")
except ValueError:
    print("Invalid age input")