integer_set = []

i = 0
while (i < 10):
    integer_set_input = int(input("Enter number: "))
    integer_set.append(integer_set_input)
    i += 1

# Positive number
positive_number_list = list()

for positive_number in integer_set:
    if (positive_number > 0):
        positive_number_list.append(positive_number)

print("Positive numbers: ", positive_number_list)

# Negative number
negative_number_list = list()

for negative_number in integer_set:
    if (negative_number < 0):
        negative_number_list.append(negative_number)

print("Negative numbers: ", negative_number_list)

# Odd number
odd_number_list = list()

for odd_number in integer_set:
    if (odd_number % 2 != 0):
        odd_number_list.append(odd_number)

print("Odd numbers: ", odd_number_list)

# Even numbers
even_number_list = list()

for even_number in integer_set:
    if (even_number % 2 == 0):
        even_number_list.append(even_number)

print("Even numbers", even_number_list)

# Number of times each number occurs in the List
number_dict = dict()

for number in integer_set:
    if number in number_dict:
        number_dict[number] += 1
    if number not in number_dict:
        number_dict[number] = 1

print("Number of time each item occurs in list", number_dict)