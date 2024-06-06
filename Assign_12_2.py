# Assign: 12
# Q. 2)

""" Write a program to accept a string from user.
Accept a second string from user to search and
find all occurrences of in the given string """

def find_occrrences(s,check):
    occurrences = []
    index = s.find(check) 
    while index != -1:  #to the end of the string
        occurrences.append(index)
        index = s.find( check, index + 1)
    return occurrences

s = input("Enter String:")
check = input("Enter the word to search: ")

# call the fucntion
result= find_occrrences(s,check)

if result:   
    print(f"The indices of the {check} is/are: ",result)
    
else:
    print(f" The {check} not found in {s}")


