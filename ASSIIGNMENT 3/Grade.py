grade_input = int(input("Enter a grade from 4 to 10: "))

if grade_input == 4:
    print("Your Grade is 'D' and Poor Performance")

elif grade_input == 5:
    print("Your Grade is 'C' and Below Average Performance")

elif grade_input == 6:
    print("Your Grade is 'C+' and Average Performance")

elif grade_input == 7:
    print("Your Grade is 'B' and Good Performance")

elif grade_input == 8:
    print("Your Grade is 'B+' and Very Good Performance")

elif grade_input == 9:
    print("Your Grade is 'A' and Excellent Performance")

elif grade_input == 10:
    print("Your Grade is 'A+' and Outstanding Performance")

else:
    print("The grade entered is not valid.")