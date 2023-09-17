n = int(input("Enter the number of terms: "))
series_sum = 0
current_term = 2
for i in range(n):
    series_sum += current_term
    current_term = current_term * 10 + 2
print("Sum of the series:", series_sum)

