# Input a password
password = input("Enter a password: ")

# Initialize variables to track requirements
length_check = False
symbol_check = False
uppercase_check = False
lowercase_check = False

# Check password requirements
if len(password) >= 5:
    length_check = True
if '&' in password:
    symbol_check = True
if any(char.isupper() for char in password):
    uppercase_check = True
if any(char.islower() for char in password):
    lowercase_check = True

# Check if all requirements are met
if length_check and symbol_check and uppercase_check and lowercase_check:
    print("Password is valid.")
else:
    print("Password is invalid.")
