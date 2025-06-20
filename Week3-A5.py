''' Assignment 5
Implement a recursive function to calculate the factorial of a non-negative integer.
Instructions:
Write a recursive function      factorial(n) that returns the factorial of the non-negative integer      n.
The factorial of      n (denoted as      n!) is defined as:
n! = n * (n-1)! for n > 0
0! = 1
Write test cases to verify the function works correctly for different values of      n.
'''


def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Test cases
def test_factorial():
    print("Testing factorial function:")
    test_cases = [0, 1, 2, 3, 4, 5, 6, 10]
    for n in test_cases:
        result = factorial(n)
        print(f"factorial({n}) = {result}")

    try:
        factorial(-1)
    except ValueError as e:
        print(f"factorial(-1) raises: {e}")

test_factorial()