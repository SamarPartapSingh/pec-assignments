

def student_data(student_id, student_name = None, student_class = None):

    print("Student ID:", student_id)

    if student_name is not None:

        print("Student Name:", student_name)
    if student_class is not None:
        print("Student Class:", student_class)

student_data(17, "samar", 10)
