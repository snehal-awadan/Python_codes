# Assign_12
# Q. 5)

""" Create a list and exchange the values as index and index as values.
lst=[12, 1, 3, 7, 8, 5, 8]
 0 1 2 3 4 5 6  """

lst=[12, 1, 3, 7, 8, 5, 8]
print("The original list is: ",lst)

# find maxi value in lst:
# we want total 13 places ==> max(lst)+1
max_value = max(lst)+1

#initialize lst1 values as (-1)
lst1 = [-1]*(max_value)

for index,value in enumerate(lst):
    lst1[value] = index

for i in range(len(lst1)):
    if lst1[i] ==-1:
        lst1[i] = i
print(lst1)
    
    
