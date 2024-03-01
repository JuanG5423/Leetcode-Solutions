import random
import sys

sys.setrecursionlimit(101000)

def bubble_sort(arr):
    for i in range(len(arr)-1):
        index = 0
        while index < len(arr)-1:
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
            index += 1
    return arr


def selection_sort(arr):
    #base case
    if len(arr) == 1:
        return arr
    else:
        #find the minimum
        min = arr[0]
        min_index = 0
        for index, number in enumerate(arr):
            if number < min:
                min = number
                min_index = index
        #swap
        arr[0], arr[min_index] = arr[min_index], arr[0]
        #add to sorted array and shrink unsorted
        return [arr[0]] + selection_sort(arr[1:])

def quick_sort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr)-1)
        pivot = arr[pivot_index]
        left = []
        right = []
        for i in range(len(arr)):
            if i != pivot_index:
                if arr[i] >= pivot:
                    right.append(arr[i])
                elif arr[i] < pivot:
                    left.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged += left[i:]
    elif j < len(right):
        merged += right[j:]
    return merged

def merge_sort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    else:
        #split the array
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        
        #recursively sort the two halves
        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)


arr = [3, 1, 5, 2, 4, 7, 6, 6, 9, 4, 2, 0, 1, 7, 3, 8, 1738]
arr2 = [6, 8, 3, 10, 5]
random_arr = [random.randint(-100, 100) for i in range(100000)]

print(merge_sort(random_arr))

'''
Time it took to sort list with 10,000 random elements from -100 to 100
Bubble sort: 13.42 seconds
Selection sort: 3.05 seconds
Quick sort: 0.36 seconds
Merge sort: 0.15 seconds

Time it took to sort list with 100,000 random elements from -100 to 100
Bubble sort: I gave up at 9 minute mark
Selection sort: Segmentation fault?
Quick sort: 2.76 seconds
Merge sort: 0.77 seconds
'''