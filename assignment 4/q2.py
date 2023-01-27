year = int(input("Enter Year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("The year is a leap year.")
        else:
            print("The year is a not leap year.")
    else:
         print("The year is a leap year.")
else:
    print("Year is not a leap year.")