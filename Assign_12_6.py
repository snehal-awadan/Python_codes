# Assign: 12
#.6)

""" Write a menu driven program to practice Set functions."""
#usermodule1.py
import sys

s1 = {10,20,30,40,50}
s2 = {40, 50, 80, 90}

print(s1)
print(s2)

print(set)
# Delete element if exists otherwise do not show any error;

def deleteElement(s1,data):
    result = s1.discard(data)
    print(s1)

#Add a element in set;
def addElement(s1,data):
    result = s1.add(data)
    print(s1)

#Create one more set;
def createNewSet():
    x = input("enter the elements to create new list (by using ,):")
    s1 = {a for a in x.split(",")}
    return s1

# perform union opeartion
def find_union():
    union_set = s1|s2
    return union_set

# perform intersection opeartion
def intersection():
    intersection_set = s1&s2
    return intersection_set

#perform differences operation
def difference():
    Difference_set = s1-s2
    return Difference_set

#convert set into frozenset
def frozenset(s1):
    frozen = frozenset(s1)
    return frozen

  
    
# Module1.py
choice = 0
while choice!=9:
    choice= int(input("""
            1. Delete element if exists otherwise do not show any error
            2. Add a elemet
            3. Create one more set
            4. Union of 2 sets
            5. Intersection of 2 sets
            6. Difference of 2 sets"
            7. Convert set into frozenset
            8. Exit
            Enter your choice: """))

    match choice:
        case 1:
            data = int(input("Enter the data to delete: "))
            deleteElement(s1,data)
        
        case 2:
             data = int(input("Enter the data to add: "))
             addElement(s1,data)           
        
        case 3:
            createNewSet()
        
        case 4:
            union_set = find_union()
            print("the union is: ",union_set)
            
            
        case 5:
            intersection_set = intersection()
            print("the intersection is: ",intersection_set)
        
        case 6:
            Difference_set = difference()
            print("the difference is: ",Difference_set)
            
        
        case 7:
            frozen = frozenset(s1)
            print("The frozenset of the given set: ",frozen)
        
        case 8:
            print("Thank You for visiting....!")
        
        case _:
            print("You have entered invalid choice")
        
        
"""incomplete"""
