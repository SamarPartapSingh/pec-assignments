date = int(input("Enter date: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

oddMonths = [1, 3, 5, 7, 8, 10, 12]

if date >= 1 and month >= 1 and year >= 1800:
    if date <= 31 and month <= 12 and year <= 2025:
        date += 1

if date > 28 and month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        date = 1
        month += 1

if date > 29 and month == 2:
    date = 1
    month += 1

elif date > 30 and oddMonths.index(month) is not int:
    date = 1
    month += 1

elif date > 31:
    date = 1
    month += 1
    if month == 12:
        date = 1
        month = 1
        year += 1

print("Next date is: ", date, "/", month, "/", year)