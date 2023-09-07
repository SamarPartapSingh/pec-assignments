# Input a string
input_string = input("Enter a string: ")

# Split the string into words
words = input_string.split()

# Capitalize the first letter of each word
capitalized_words = [word[0].upper() + word[1:] for word in words]

# Join the words back into a string
capitalized_string = " ".join(capitalized_words)

# Print the capitalized string
print("Capitalized string:", capitalized_string)
