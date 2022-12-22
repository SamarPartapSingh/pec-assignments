given_string = "Python is a case sensitive language"

print("Length of string:", len(given_string))

print("String Reversed:", given_string [::-1])

sliced_string = given_string [slice(10,27)]
print("Sliced String is:", sliced_string)

replaced_string = given_string.replace("a case sensitive", "object oriented")
print("String replaced 'a case sensitive' with 'object oriented' is:", replaced_string)

print("Index of substring 'a':",given_string.index("a"))

removed_whitespaces_string = given_string.replace(" ","")
print("String with removed whitespaces:",removed_whitespaces_string)