def challan(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return "No Challan"
    elif 61 <= speed <= 80:
        return "Small Challan"
    else:
        return "Heavy Challan"

speed = 65
birthday = True  # Change this to False if it's not your birthday
result = challan(speed, birthday)
print(result)  # This will print "Small Challan" if it's your birthday and speed is 70

