'''

Assignment 9
Explain the Merge Sort algorithm and demonstrate its implementation in Python to sort a list of strings in alphabetical order.
Give an example

'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].lower() < right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

words = ["Banana", "apple", "Cherry", "date"]
sorted_words = merge_sort(words)
print("Sorted list:", sorted_words)
