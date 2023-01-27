lower_bound = int(input("Enter lower bound of the range:"))
upper_bound = int(input("Enter upper bound of the range:"))

if (lower_bound > upper_bound):
    print("Switching the bounds due to lower bound being greater than upper bound.")
    temp_lower_bound = upper_bound
    upper_bound = lower_bound
    lower_bound = temp_lower_bound

divisior = int(input("Enter the divisor:"))

divisible_exist = False

for i in range(lower_bound, upper_bound + 1):
    if i % divisior == 0:
        print(i, "is divisible by", divisior)
        divisible_exist = True

if not divisible_exist:
    print("No numbers are divisible!")