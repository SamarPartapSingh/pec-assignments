# Input the first list
list1_input = input("Enter the first list (items separated by space): ")
list1 = list1_input.split()

# Input the second list as a string of numbers separated by space
list2_input = input("Enter the second list (numbers separated by space): ")

# Split the second list into a list of numbers
list2 = [int(x) for x in list2_input.split()]

# Append the second list to the first list
list1 += list2

print("Combined list:", list1)

