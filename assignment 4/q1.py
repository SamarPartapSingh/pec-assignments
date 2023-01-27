marks = int(input("Enter Marks: "))

list_of_grade = ["A", "B", "C", "D", "E", "F"]

if (marks > 0):
    if (marks > 80):
        print("The grade is", list_of_grade[0])
    if (marks > 60 and marks < 80):
        print("The grade is", list_of_grade[1])
    if (marks > 50 and marks < 60):
        print("The grade is", list_of_grade[2])
    if (marks > 45 and marks < 50):
        print("The grade is", list_of_grade[3])
    if (marks > 25 and marks < 45):
        print("The grade is", list_of_grade[4])
    if (marks < 25):
        print("The grade is", list_of_grade[5])