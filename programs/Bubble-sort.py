
# Bubble-sort steps : 
# steps :
# 1. Loop to access to each elements of the array:

# 2. Loop second we need to compare elements with each other.

# 3. compare two adjacent elements 
# 4. change > to < to sort in decending order.

# 5. Swap elements if elements are not in intended order :

# writing an algorithm for bubble sort. 
def bubblesort(array):
    # 1. Loop to access to each elements of the array:
    for i in range(len(array)):
        # 2. Loop second we need to compare elements with each other.
        for j in range(0, len(array) - i - 1):
            # 3. compare two adjacent elements 
            if array[j] > array[j + 1]:

                # 5. Swap elements if elements are not in intended order.
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

data = [-2, 45, 0, 11, -9]
bubblesort(data)
data

print('sorted data in decending order :', data)


array2 = ['k', 'l', 'z', 'm', 'o', 't', 'a']
bubblesort(array2)
array2



