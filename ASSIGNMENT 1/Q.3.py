#To find out how many minutes and seconds are there in given amount of seconds

try:
    #Get raw seconds input
    seconds_raw = eval(input("Enter Number of seconds: "))

    #get time from raw seconds
    minutes = int(seconds_raw / 60)
    seconds = seconds_raw % 60

    #display output
    print(seconds_raw, "seconds have ", minutes, "minutes and ", seconds, "seconds.")

except:
    print ("The data entered is invalid. Exiting Application...")