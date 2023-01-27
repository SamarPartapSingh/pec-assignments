lower_bound = int(input("Enter lower bound of the range:"))
upper_bound = int(input("Enter upper bound of the range:"))

if (lower_bound > upper_bound):
    print("Switching the bounds due to lower bound being greater than upper bound.")
    temp_lower_bound = upper_bound
    upper_bound = lower_bound
    lower_bound = temp_lower_bound

primes = []

for i in range(lower_bound, upper_bound + 1):

    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)

print(primes)