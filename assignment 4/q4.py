for number_of_candies in range(1,200,1):
    if number_of_candies % 5 == 2 and number_of_candies % 6 == 3 and number_of_candies % 7 == 2:
        print("The number of candies is:", number_of_candies)
        break