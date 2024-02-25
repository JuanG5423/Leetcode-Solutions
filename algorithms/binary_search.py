def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        elif target == arr[mid]:
            return mid
    return -1

print(binary_search([1, 2, 3, 4, 4, 5], 4))