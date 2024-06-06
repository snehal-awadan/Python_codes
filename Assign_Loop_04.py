# Assign :"List"
# Q. 04)

list1=["Hello","Welcome"]
list2=["students","Sir","professor"]
new = []

for i in range (0,len(list1)):
    for j in range (0,len(list2)):
        new.append((list1[i])+ " " +(list2[j]))
print(new)
        
