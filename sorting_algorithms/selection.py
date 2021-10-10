"""
Selection
Time Complexity O(n^2)
"""

import numpy as np

np.random.seed()

def insertion_sort(arr):
    x = np.shape(arr)[0]
    for k in range(x):
        for i in range(x-1,0,-1):
            k = arr[i]
            j = i - 1

            while k < arr[j] and j >= 0:
                arr[j+1] = arr[j]
                j = j - 1

            arr[j+1] = k
    
    return arr

if __name__ == '__main__':
    p = np.random.randint(1,100,5)
    print(f'Generated Array: {p}')

    y = insertion_sort(p)
    print(f'Insertion Sorted Array: {y}')