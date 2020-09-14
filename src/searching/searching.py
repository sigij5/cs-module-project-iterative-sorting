def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1
    midpoint = 0

    while left <= right:
        midpoint = (right + left) // 2

        if target == arr[midpoint]:
            return midpoint
        elif target < arr[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1


    return -1  # not found



# takes a sorted array as input and a target to search for
# and returns the index of the target in the array if it exists, or -1 if it is not in array

# def binary_search(arr, target):
#     #find the midpoint element (len // 2)
#     left = 0
#     right = len(arr)

#     # keep iterating so long as left <= right
#     while left <= right:
#         midpoint = (right + left) // 2

#         if arr[midpoint] == target:
#             return midpoint
#         elif arr[midpoint] < target:
#             # toss out the left side of the array
#             # toss out the midpoint element itself as well
#             left = midpoint + 1
#         else:
#             right = midpoint - 1

#     # we didn't find target
#     return -1

