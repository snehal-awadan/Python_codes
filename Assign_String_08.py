# Assign: "String"
# Q.08)

""" Define a function overlapping() that takes two lists and returns True if they have at least one
member in common, False otherwise. """


def overlapping(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                return 1
            else:
                return 0


l1 = input("Enter elements of the list separated by space: ")
elements = l1.split()

l2 = input("Enter elements of the list separated by space: ")
elements = l2.split()
print(l1)
print(l2)

l1 =len(l1)
l2 =len(l2)
# call the function:
if overlapping(l1,l2) == 1:
    print("result is true")
else:
    print("result is false")
