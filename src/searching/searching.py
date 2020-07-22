# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start >= end:
        return -1

    middle = (start + end) // 2
    if arr[middle] == target:
        return middle
    elif target < arr[middle]:
      return binary_search(arr,target,start,middle + 1)
    else:
      return binary_search(arr,target,middle - 1,end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    first = 0
    last = (len(arr) - 1)
    found = False
    ascending = True
    if arr[0] > arr[1]:
        ascending = False
        arr = arr[::-1]

    while first <= last and not found:
        middle = (first + last) // 2

        if arr[middle] == target:
            found = True
            if ascending == True:
                return middle
            else:
                return (len(arr) - 1) - middle 
        else:
            if target < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return -1
