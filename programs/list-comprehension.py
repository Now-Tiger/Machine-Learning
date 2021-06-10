
list1 = [23, 4, 5,15, 8, 77, 42, 57, 90, 85, 13, 22]
list1

even = []
for x in list1:
    if x%2 == 0:
        even.append(x)
print(even) 

# ********************************************************************************
# List comprehensions :

new_list = [ x for x in list1 if x % 2 == 0]
new_list

new_list2 = [x for x in list1 if x%2 == 0 if x < 40]
new_list2

# ********************************************************************************

new_data = [ 1 if x % 2 == 0 else 0 for x in list1]
new_data

# ********************************************************************************