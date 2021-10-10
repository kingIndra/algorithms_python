#This does not work

"""
Insertion Sort
Time Complexity O(n^2)
"""
def insertion_sort(arr):
    x = len(arr)
    for i in range(x-1,0,-1):
        k = arr[i]
        j = i - 1
        
        while k < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j+1] = k
    
    return arr
    