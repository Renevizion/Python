'''
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''

char_input = input ("Please enter a single character: ")


if len(char_input) == 1 and char_input.isalpha():

    # convert the input to lowercase
    char = char_input.lower()

    # check for the values

    if char in 'aeiou':
        print("The character is a vowel")
    else:
        print("The character is a consonant!")

else:
    # handle cases that are not a single character
    if len(char_input) != 1:
        print("Error: Please enter only one character.")
    else:
        print("Error: The input is not a letter")