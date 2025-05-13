import math


def is_prime(number):
    # Check if the number is at least 1
    if number <= 1:
        print("Not Prime")
        return

    # 2 and 3 are prime numbers
    if number <= 3:
        print("Prime")
        return

    # Eliminate even numbers and multiples of 3
    if number % 2 == 0 or number % 3 == 0:
        print("Not Prime")
        return

    limit = math.isqrt(number)
    i = 5

    # Loop to check divisibility up to the square root of the number
    while i <= limit:
        if number % i == 0 or number % (i + 2) == 0:
            print("Not Prime")
            return
        i += 6

    print("Prime")


# Call the function
is_prime(97)
