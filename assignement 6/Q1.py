def is_number_perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(is_number_perfect(10))
print(is_number_perfect(6))