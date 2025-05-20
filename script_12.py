'''

Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.
=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.

'''

def print_triangle(rows: int, char: str):
    for i in range(1, rows + 1):
        for j in range(i):
            print(char, end='')
        print()  

# ask for user input
num_rows = int(input("Enter the number of rows for the triangle pattern: "))
pattern_char = input("Enter the character to use for the pattern: ")

# Output pattern
print_triangle(num_rows, pattern_char)
