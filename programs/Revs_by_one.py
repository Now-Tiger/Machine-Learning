
# Function to left rotate an array by d = d is index number
def leftrotate(arr, d, n):            
    for i in range(d):
        leftByOne(arr, n)

def leftByOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

def printArray(arr, size):
    for i in range(size):
        print("% d"% arr[i], end =" ")

arr = [1, 2, 3, 4, 5, 6, 7]
leftrotate(arr, 2, 7)
printArray(arr, 7) 

arr = [2, 8, 5, 6, 1, 3, 4]
leftrotate(arr, 4, 7)
printArray(arr, 7)

# o/p : 1, 3, 4, 2, 8, 5, 6


# Time Complexity : O(n*d)
# Auxillary Complexity : O(1)
