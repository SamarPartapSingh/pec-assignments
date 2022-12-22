list_of_numbers = [3, 9, 10]

list_of_tuples = [tuple()] * len(list_of_numbers)


for i in range(0, len(list_of_numbers)):
    list_of_tuples[i] = tuple((list_of_numbers[i], (list_of_numbers[i] * list_of_numbers[i])))

print(list_of_tuples)