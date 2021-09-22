
"""
Binary Search
Time Complexity of Worst case is O(n*log(n))
The array should be sorted in an ascending order.
Pass 0 (Zero) for the parameter "l", and size of the array should be passed for "r".
"""

def binary_search(array, key) -> bool:
    l = 0
    r = len(array)
    
    while l < r:
        mid = int((l+r)/2)
        
        if key == array[mid]:
            return True
        elif key < array[mid]:
            r = mid - 1
        elif key > array[mid]:
            l = mid + 1
            
    return False

def binary_recur(array, key, l, r) -> bool:
    if l > r:
        return False
    
    mid = int((l+r)/2)
    
    if key == array[mid]:
        return True
    elif key < array[mid]:
        return binary_search_recur(array, key, l, mid - 1)
    elif key > array[mid]:
        return binary_search_recur(array, key, mid + 1, r)
    