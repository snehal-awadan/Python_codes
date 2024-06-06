# Assign : 11
# Q.8)

def find_longest_word(lst):
    long_len = 0
    for word in lst:
        length = len(word)
        if length > long_len:
            long_len = length
    return long_len

lst = []
num = int(input("how many words you want to enter: "))
for i in range(num):
    word = input(f"Enter word {i+1}: ")
    lst.append(word)
print(lst)

#call the function
result = find_longest_word(lst)
print("The longest len is : ",result)



