my_list = [1, 2, 3, 4, 5]

while True:
    print("Current List:", my_list)
    print("1. Insert Element")
    print("2. Delete Element")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to insert: "))
        position = int(input("Enter the position to insert: "))
        my_list.insert(position, value)
    elif choice == 2:
        delete_choice = int(input("1. Delete by value\n2. Delete by position\n3. Delete a slice\nEnter delete choice: "))
        if delete_choice == 1:
            value = int(input("Enter the value to delete: "))
            if value in my_list:
                my_list.remove(value)
            else:
                print("Value not found in the list.")
        elif delete_choice == 2:
            position = int(input("Enter the position to delete: "))
            if 0 <= position < len(my_list):
                del my_list[position]
            else:
                print("Invalid position.")
        elif delete_choice == 3:
            start = int(input("Enter the start position of the slice: "))
            end = int(input("Enter the end position of the slice: "))
            if 0 <= start <= end < len(my_list):
                del my_list[start:end + 1]
            else:
                print("Invalid slice range.")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
