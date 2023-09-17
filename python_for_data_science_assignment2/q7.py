a = input("string: ")
words = a.split()

def count_dog(string_list):
    count = 0
    for word in string_list:
        if word == 'dog':
            count += 1
    return count

print(count_dog(words))




