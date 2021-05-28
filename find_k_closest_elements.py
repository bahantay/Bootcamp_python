import bisect
from bisect import bisect_left

def find_k_closest_elements(arr, k, x):
    m = bisect.bisect_left(arr, x)
    res = []
    counter = 0
    l, r = m-1, m
    
    while counter < k and l >= 0 and r < len(arr):
        if abs(arr[l]-x) <= abs(arr[r]-x):
            res = [arr[l]] + res
            l -= 1
        else:
            res.append(arr[r])
            r += 1
        counter += 1
    
    while counter < k and l >= 0:
        res = [arr[l]] + res
        l -= 1
        counter += 1
    while counter < k and r < len(arr):
        res.append(arr[r])
        r += 1
        counter += 1
    return res

arr = [1,2,3,4,5]
k = 4
x = 3
print (find_k_closest_elements(arr, k, x))
