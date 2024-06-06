# Assign : 11
# Q.9)

def filter_long_words(lst,n):
    long_word = []
    for word in lst:
        if len(word)>n:
            long_word.append(word)
    return long_word


lst = []
num = int(input("how many words you want to enter in list: "))
for i in range(num):
    element = input(f"enter element {i+1}: ")
    lst.append(element)
print(lst)

n= int(input("Enter an interger: "))

#call the function
print(f"the elements greater that {n} are: ",filter_long_words(lst,n))
