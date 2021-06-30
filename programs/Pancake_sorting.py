'''
* Given an unsorted array, sort the given array. You are allowed to do only following operation on array. 
* flip(arr, i): Reverse array from 0 to i 

1. Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible, the 
 goal is to sort the sequence in as few reversals as possible. 

2. The idea is to do something similar to Selection Sort. We one by one place maximum element at the end and 
 reduce the size of current array by one. 

 steps :
 Start from current size equal to n and reduce current size by one while it’s greater than 1. Let the current size be curr_size. Do following for every curr_size
 1. Find index of the maximum element in arr[0..curr_szie-1]. Let the index be ‘mi’
 2. Call flip(arr, mi)
 3. Call flip(arr, curr_size-1)
'''

# Reverse array[0...1]
def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
# Returns index of maximum element in arr[0...1]
def findMax(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i]>arr[mi]:
            mi = i
    return mi 
# The main function that sorts given array using flip operations
def pancakesort(arr, n):
    # Start from the complete array and one by one reduce current size by one 
    curr_szie = n
    while curr_szie > 1:
        # Find index of the maximum element in arr[0..curr_size-1]
        mi = findMax(arr, curr_szie)
        # # Move the maximum elementto end of current arrayif it's not already atthe end
        if mi != curr_szie-1:
            flip(arr, mi)
            flip(arr, curr_szie-1)
        curr_szie -= 1

def printArray(arr, n):
    for i in range(0,n):
        print('%d'%(arr[i]), end=' ')

arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
pancakesort(arr, n);
print ("Sorted Array ")
printArray(arr,n)