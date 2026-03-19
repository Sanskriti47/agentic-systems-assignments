try:
    # Take user input
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    #Check for negative age 
    if age<0:
        print("Age cannot be negative")
    else:
        # Print greeting
        print("Hello,",name)
        # Determining the age category 
        if age<13:
            print("You are a Child")
        elif age>=13 and age<=17:
            print("You are a Teenager")
        elif age>=18 and age<=59:
            print("You are an Adult")
        else:
            print("You are a Senior Citizen")
            # Voting eligibilty 
        if age>=18:
            print("You are eligible to Vote")
        else:
            print("You are Not eligible to Vote")
            # Handle invalid age input 
except ValueError:
    print("Invalid age input")

