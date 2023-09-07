# Input a string
input_string = input("Enter a string: ")

# Initialize counters
alphabets = digits = symbols = uppercase = lowercase = 0

# Analyze the string
for char in input_string:
    if 'a' <= char <= 'z':
        alphabets += 1
        lowercase += 1
    elif 'A' <= char <= 'Z':
        alphabets += 1
        uppercase += 1
    elif '0' <= char <= '9':
        digits += 1
    else:
        symbols += 1

# Print the information
print("Number of Alphabets:", alphabets)
print("Number of Digits:", digits)
print("Number of Symbols:", symbols)
print("Number of Uppercase Alphabets:", uppercase)
print("Number of Lowercase Alphabets:", lowercase)

