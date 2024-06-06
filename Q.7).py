# Assign : 11
# Q.7)

def overlapping(lst1,lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                return True
            else:
                return False


lst1 = input("enter the elements for lst 1: ").split()
lst2 = input("enter the elements for lst 2: ").split()

print(lst1)
print(lst2)

#call the function;
result = overlapping(lst1,lst2)
print(result)
