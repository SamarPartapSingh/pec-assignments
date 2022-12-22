#To find greatest of three numbers

#Try to use input to evaulate the greatest of the numbers
try:
    #Get input from user
    a = eval(input("Enter number 1: "))
    b = eval(input("Enter number 2: "))
    c = eval(input("Enter number 3: "))

    #Compare inputs
    if a > b and a > c:
        print(a, "is the greatest")
    if b > a and b > c:
        print(b, "is the greatest")
    if c > a and c > b:
        print(c, "is the greatest")
    print("Program exited with code 0.")


#Throw exception if number is invalid
except:
    print ("Enter a valid number!")
    print("Program exited with code 1.")