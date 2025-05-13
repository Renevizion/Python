'''
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''


try:
    hours = float(input("Enter time duration in hours: "))

    if hours < 0:
        print("Error: Please enter a non-negative number for hours.")
    else:
        minutes = hours * 60
        seconds = hours * 3600


        print("Time in minutes:", minutes)
        print("Time in seconds:", seconds)

        # or

        print(f"Time in minutes is {minutes:.2f} which is equal to {seconds:.2f} seconds ")



except ValueError:
    print("Error: Please enter a valid number.")
