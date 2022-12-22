# To calculate Income Tax

try:
    # Get gross income
    income = eval(input("Enter Gross Income: "))

    standard_deduction = 10000  # Standard Deduction

    # Get number of dependents
    dependents = eval(input("Enter Number of dependents: "))
    dependent_deduction = 3000  # Deduction on each individual dependent

    # Calculate taxable income
    taxable_income = income - standard_deduction - (dependent_deduction * dependents)

    # Prevent taxable income to go into negative
    if (taxable_income < 0):
        taxable_income = 0

    # Display taxable income
    print("Taxable income is: ", taxable_income)

    print("Therefore tax applicable is: ", taxable_income * 0.2)

except:
    print("The data entered is invalid. Exiting Application...")