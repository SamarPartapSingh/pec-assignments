input_string = str("ABCDEFGHIJK")

for i in range(0, 6):
    print(" " * i, input_string[0: (11 - (2*i))])