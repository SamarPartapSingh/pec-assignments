#input marks for 3 subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# Calculate the average
average = (subject1 + subject2 + subject3) / 3

# Check if average is greater than or equal to 40
if average >= 40:
    print("Pass")
else:
    print("Fail")
