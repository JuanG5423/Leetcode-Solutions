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

'''
Selection sort example:
[3, 1, 2, 4]
Base case not reached, find the minimum value and swap it with the left
[1, 3, 2, 4] 
We know 1 is in the right place, put it in its own list and combine it with selection sort([3, 2, 4])
[3, 2, 4]
Base case not reached, find the minimum value and swap it with the left
[2, 3, 4]
We know 2 is in the right place, put it in its own list and combine it with selection sort([3, 4])
[3, 4]
Base case not reached, find the mimimum value and swap it with the left
[3, 4]
We know 3 is in the right place, put it in its own list and combine it with selection sort([4])
Base case reached, return [4]
Combine [3] and [4] = [3, 4]
Combine [2] and [3, 4] = [2, 3, 4]
Combine [1] and [2, 3, 4] = [1, 2, 3, 4]
'''


arr = [3, 1, 5, 2, 4, 7, 6]
arr2 = [3, 1, 2, 4]

print(selection_sort(arr))






#first split from 0 to 3 and 4 to 6, length 7
#[3, 1, 2, 4] should split from 0 to 1 and 2 to 3, length 4
#return [arr[:len(arr)//2 + 1], arr[len(arr)//2 + 1:]] for odd lengths, [arr[:len(arr)//2], arr[len(arr)//2:]]