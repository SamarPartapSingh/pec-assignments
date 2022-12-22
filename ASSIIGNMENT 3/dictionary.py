#Dictionary containing raw student data
student_dict = {}

#Dictionary containing SID sorted student data
sid_sorted_student_dict = {}

#Dictionary containing Name sorted student data
name_sorted_student_dict = {}

#Integer used to manage the option input for non student data entry prompt
option = int(10)

#while loop for reoccuring prompt
while (option != 0):

    #Option input used for entering of student data
    data_option = str(input("Enter student data? (Y/N):"))

    #Code block for data entry
    if (data_option == "Y"):
        _sid = int(input("Enter SID: "))                #Get SID
        _name = str(input("Enter student name: "))      #Get Name
        student_dict[_sid] = _name                      #Add SID and Name into the dictionary as a Key-Value Pair

    #Code block for operations on the student_dict
    if (data_option == "N"):

        print("1) Print student details in dictionary")
        print("2) Sort dictionary by student names")
        print("3) Sort dictionary by SID")
        print("4) Search")
        print("0) Exit")

        option = int(input("Enter an option: "))

        if (option == 1):
            #Print raw student data
            print(student_dict)

        elif (option == 2):
            #Sort student data by name

            #Get items in the dict (i.e. student_dict.items()), create a new small (lambda) function for the sorting mechanism of the sorted() function
            name_sorted_student_dict = dict(sorted(student_dict.items(), key = lambda x : x[1]))
            print(name_sorted_student_dict)

        elif (option == 3):
            #Sort student data by SID(Key) by iterating for each SID present in student_dict in ascending order
            for i in sorted(student_dict):
                sid_sorted_student_dict[i] = student_dict[i]
            print(sid_sorted_student_dict)

        elif (option == 4):
            #Search by SID
            _search_sid = int(input("Enter SID to search: "))
            print(student_dict[_search_sid])
        elif (option == 0):
            print("Exiting Application...")
        else:
            print("Enter valid option")