# Assign :"List"
# Q. 10)

list = [5,20,15,20,25,50,20]
print(list)

num = 20
for i in list:
    if i == num:
        list.remove(num)
print("After removing 20 from the list: ",list)
