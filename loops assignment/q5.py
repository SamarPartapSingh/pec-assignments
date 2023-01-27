rows = int(input("Enter number of rows to be input:"))

count = 0

for i in range(0, rows):
    for j in range(0, i + 1):
        if (count >= 26):
            count = 0
        print(chr(65 + count), end = '')
        count += 1
    print("")