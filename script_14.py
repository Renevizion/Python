'''

Challenge: Handle negative exponents efficiently.
====================================
Description: Develop a function named      power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.
'''


base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

def power(base, exponent):

    # Handle zero exponent
    if exponent == 0:
        return 1

    result = 1

    # Handle positive exponent
    if exponent > 0:
        for _ in range(exponent):
            result *= base

    # Handle negative exponent
    else:
        for _ in range(-exponent):
            result *= base
        result = 1 / result  # Take reciprocal for negative exponents

    return result

print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")

