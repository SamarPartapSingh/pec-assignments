fibonacci = []

number_of_fibonacci = int(input("Enter number of Fibonnaci numbers for the sequence: "))

u, v = 0, 1
for i in range(0, number_of_fibonacci):
    u, v = v, u + v
    fibonacci.append(v)

print(fibonacci)
print(sum(fibonacci) / number_of_fibonacci)