'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''


length = float(input('Please enter length: '))
width = float(input('Please enter width: '))

area = length * width

if area <= 0:
    print ("Please use a positive number.")
else:
    print("the area is:", area)