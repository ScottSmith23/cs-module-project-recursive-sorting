# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    for e in range(0,elements):

        if 0 == len(arrA):
            merged_arr[e] = arrB[0]
            arrB.pop(0)

        elif 0 == len(arrB):
            merged_arr[e] = arrA[0]
            arrA.pop(0)

        elif arrA[0] < arrB[0]:
            merged_arr[e] = arrA[0]
            arrA.pop(0)

        else:
            merged_arr[e] = arrB[0]
            arrB.pop(0)


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)

    arr = merge(left,right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    # Your code here
    startr = mid + 1

    if len(arr) <= 1:
        return arr

    while start <= mid and startr <= end:
        if arr[start] <= arr[startr]:
            start += 1
        else:
            value = arr[startr]
            index = startr
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value
            start += 1
            mid += 1
            startr += 1


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) <= 1:
        return arr

    if l < r:

        mid = (l + r) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)

        merge_in_place(arr, l, mid, r)

        return arr

