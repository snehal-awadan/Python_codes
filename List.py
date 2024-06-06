# List: it is mutable, iterable, allowed duplicates.

lst = []
print("This is empty list:",lst)

#append : we can add element at the last;
lst.append(10)
print("After adding element at the last:",lst)

#we can add nested list in the list;
lst.append([50,60,71])
print("After appending nested list: ",lst)

#we can add multiple different value;
lst.append('abc')
print("After appending differnt value: ",lst)

#extend : we can add multiple elements at the last;
lst.extend([20,30,40])
print("After appending multiple elements at the last: \n ",lst)

#pop(): we can delete element from the end;
lst.pop()
print("After deleting last element:",lst)

lst.append(20)
print(lst)

#pop(position) : we can delete element by giving position;
lst.pop(0)
print("After deleting element by position: ",lst)

#remove(position) : we will delete the first occrrence of the element;
lst.remove(20)
print("After deleting by remove: ",lst)

# Function in list:

# index : to find the position of the element;
print("Position of the given element",lst.index(20))

#if value is not found-->Throws an exception

#count : find the no of occurrences;
print("COunt of given element",lst.count(20))

#reverse: to reverse the original list;
lst2 = [60,20,30,40,50]
print("New list: ",lst2)
print("After reversing the list:",lst2.reverse())

#sort: it will sort the element in ascending order
#       If the list contains only homogenous element;

print("After sorting:",lst2.sort())

# we can sort in decending order alos;
print("After sorting:",lst2.sort(reverse=True))

#copy():
lst3 = lst.copy()
print("After copying lst list:",lst3)

