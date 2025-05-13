try:
    year_input = int(input("Enter a year: "))

    if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
        print(f"{year_input} is a leap year.")
    else:
        print(f"{year_input} is not a leap year.")
except ValueError:
    print("Please enter a valid number for the year.")