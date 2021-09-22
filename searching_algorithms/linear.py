"""
Linear Search
Time Complexity of Worst case is O(n)
and size
of the array should be passed for the "end" parameter.
"""

def linear_s(array, key) -> bool:
    for x in arr:
        if x == key:
            return True
    
    return False

def linear_recur(array, key, r, l=0) -> bool:
    if l == r:
        return False
    elif array[l] == key:
        return True 
    else:
        return linear_recur(array,key,r, l+1)