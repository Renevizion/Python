'''

What is the time complexity of the Quick Sort algorithm, and how would you implement it in Python?
Give an example
>>>>
Best and avg: O(n log n)

Worst: O(n²)



'''


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

numbers = [7, 3, 1, 9, 4]
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
