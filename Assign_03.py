# Assign : 15
# Q.3)

import re

def patternMatch(string, pattern1, pattern2):
    if re.match(pattern1,string):
        return 1
    elif re.match(pattern2, string):
        return 2
    else:
        return 3

pattern1 = input("enter the pattern: ")
pattern2 = input("enter the another pattern: ")

list1 =[]
list2 =[]

print("enter strings: (type exit to stop")
      
while True:
    string = input("enter string: ")
    if string.lower() == "exit":
        break
    # call the function
    result = patternMatch(string, pattern1, pattern2)
    if result ==1:
        list1.append(string)
    elif result == 2:
        list2.append(string)
    else:
        print("pattern not match..")
    

print("the list which match with pattern1: ",list1)
print("the list which match with pattern2: ",list2)



    
