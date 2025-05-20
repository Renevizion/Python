'''

Assignment 16
Challenge: Optimize the function to handle large input lists efficiently.
==============================
Description: Develop a function called      find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.

'''

# find common elements in two lists
def find_common_elements(list1, list2):
    result = []

    for item in list1:
        if item in list2:
            if item not in result:
                result.append(item)

    return result

