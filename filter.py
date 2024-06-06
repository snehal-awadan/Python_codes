# filter() function:

def fun(numbers):
    num = [1,3,5,7,9,11]
    
    if (numbers in num):
        return True
    else:
        return False
        
sequence = [1,2,3,4,5,6,7,8,9,10]

# use filter funciton'
result=filter(fun,sequence)
print("the filtered numbers are: ")

for s in result:
    print(s)
