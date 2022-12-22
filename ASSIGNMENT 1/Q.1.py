# To find average of three numbers

# Try to use input to evaulate the greatest of the numbers
try:
    # Get input from user
    a = eval(input("Enter Number 1: "))
    b = eval(input("Enter Number 2: "))
    c = eval(input("Enter Number 3: "))

    # Find average
    avg = (a + b + c) / 3

    # Display output
    print("Average of given three numbers is:", avg)

# Throw exception if number is invalid
except:
    print("The data entered is invalid. Exiting Application...")