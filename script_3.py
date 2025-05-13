'''Assignment 3
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.'''

weight_input = float(input("Enter your weight in kilos: "))
height_input = float(input("Enter your height in meters: "))

weight = float(weight_input)
height = float(height_input)

bmi = weight / (height ** 2)
print("The BMI is: ", bmi)

