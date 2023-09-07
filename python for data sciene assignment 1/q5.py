# Input a string of numbers separated by space
input_string = input("Enter numbers separated by space: ")

# Split the input string into a list of numbers
numbers = [int(x) for x in input_string.split()]

# Selection sort algorithm
for i in range(len(numbers)):
    min_idx = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    # Swap the elements
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print("Sorted list:", numbers)
