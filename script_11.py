'''
Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non-numeric input.
=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1.

'''

def collatz_sequence():
    while True:
        user_input = input("Enter a positive integer: ")

        try:
            number = int(user_input)
            if number <= 0:
                print("Please enter a number greater than 0.")
                continue
            break  # valid input, exit loop
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("Collatz sequence: ")
    print(number)

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)

collatz_sequence()
