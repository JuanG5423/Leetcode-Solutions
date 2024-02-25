#Problem: Given an array of integers, find the maximum sum of a contiguous subarray of size k.
'''     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
Input: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0], k = 3
Output: 16 (Subarray [7, 8, 1] has the maximum sum)
'''

def sliding_window(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr)-k+1):
        local_sum = sum(arr[i:i+k])
        if local_sum > max_sum:
            max_sum = local_sum
    return max_sum



print(sliding_window([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))
