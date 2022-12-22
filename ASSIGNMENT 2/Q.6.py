try:
    side_a = eval(input("Enter the first side of the triangle:"))
    side_b = eval(input("Enter the second side of the triangle:"))
    side_c = eval(input("Enter the third side of the triangle:"))

    if (side_a + side_b) > side_c:
        if (side_b + side_c) > side_a:
            if (side_a + side_c) > side_b:
                print("Yes")

            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

except:
    print("Invalid value entered. Exiting application...")