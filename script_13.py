'''

Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

'''


def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True

# ask for user input
user_input = input("Enter a string to check if it's a palindrome: ")

# normalize input: lowercase and remove spaces
normalized = ''.join(user_input.lower().split())

# check and print result
if is_palindrome(normalized):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
