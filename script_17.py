'''

Assignment 17
Challenge: Ensure that the function works correctly with tuples of different lengths.
=============================================
Description: Create a function called      concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.

'''


# Add two tuples together
def concat_tuples(t1, t2):
    return t1 + t2


first = (1, 2, 3)
second = (4, 5)
new_tuple = concat_tuples(first, second)
print("Combined tuple:", new_tuple)
