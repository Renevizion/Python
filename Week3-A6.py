''' Implement a recursive function to compute the nth Fibonacci number.
Instructions:
Write a recursive function      fibonacci(n) that returns the nth Fibonacci number.
The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Write test cases to verify the function works correctly for different values of      n.

'''



def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases
def test_fibonacci():
    print("Testing fibonacci function:")
    test_values = list(range(11))  # 0 to 10
    expected_results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    for i, expected in zip(test_values, expected_results):
        result = fibonacci(i)
        print(f"fibonacci({i}) = {result} (Expected: {expected})")

    # Negative test
    try:
        fibonacci(-1)
    except ValueError as e:
        print(f"fibonacci(-1) raises: {e}")

test_fibonacci()