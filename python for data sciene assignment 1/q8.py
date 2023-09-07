# Input a string
input_string = input("Enter a string: ")

# Define a set of consonants
consonants = set("bcdfghjklmnpqrstvwxyz")

# Initialize variables
longest_subsequence = ""
current_subsequence = ""

# Iterate through the input string
for char in input_string:
    if char.lower() in consonants:
        current_subsequence += char
    else:
        if len(current_subsequence) > len(longest_subsequence):
            longest_subsequence = current_subsequence
        current_subsequence = ""

# Check the last subsequence
if len(current_subsequence) > len(longest_subsequence):
    longest_subsequence = current_subsequence

# Print the longest common subsequence
print("Longest Common Consonant Subsequence:", longest_subsequence)
