"""Bubble Sort
    Time Complexity O(n^2)
    """

def bubble_sort(arr):
    x = len(arr)
    for i in range(x-2):
        for j in range(0, x-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr