input_string = str(input("Enter a string: "))
if input_string.find(" ") != -1:
    string_to_find = str(input("Enter the string to find: "))
else:
    string_to_find = str(input("Enter a letter to find:"))

print(input_string.count(string_to_find))