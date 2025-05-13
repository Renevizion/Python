'''
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
'''


def get_valid_mark(subject_num):
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {subject_num} (0–100): "))
            if 0 <= mark <= 100:
                return mark
            print("Error: Marks must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Collect marks using a loop
marks = [get_valid_mark(i + 1) for i in range(3)]

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Output
print(f"\nAverage Marks: {average:.2f}")
print(f"Grade: {grade}")
