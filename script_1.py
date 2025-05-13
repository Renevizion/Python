

# Prompt user to enter principal amount
principal = float(input("Enter the principal amount: "))

# prompt the user to enter the interest rate
rate = float(input("Enter the interest rate (in percentage): "))

# prompt the user to enter the time period
time = float(input("Enter the time period: "))

# processing is below
simple_interest = (principal * rate * time) / 100

# output

print("The calculated interest rate is: ", simple_interest)