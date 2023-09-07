# Input an integer
decimal_number = int(input("Enter an integer: "))
binary_representation = ""

# Handle negative numbers separately
if decimal_number < 0:
    binary_representation = '-'
    decimal_number = abs(decimal_number)

# Convert to binary
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_representation = str(remainder) + binary_representation
    decimal_number //= 2

# Print the binary equivalent
print("Binary Equivalent:", binary_representation)

