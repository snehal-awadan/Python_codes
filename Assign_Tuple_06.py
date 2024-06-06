# Assign: "Tuple"
# Q. 06)

tuple1 = (11, [22, 33], 44, 55)
print(tuple1)

#convert tuple into list
list = list(tuple1)
list[1][0] = 200
#convert list into tuple
new = tuple(list)
print(list)
