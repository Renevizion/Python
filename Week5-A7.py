'''


How would you implement the Bubble Sort algorithm in Python to sort a list of numbers in ascending order?
Give an exmaple



'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [5, 2, 9, 1, 3]
bubble_sort(numbers)
print("Sorted list:", numbers)
