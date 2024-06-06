#Assign : "String"
# Q. 07)

def sum(x):
    if x == 1:
        return 1
    else:
        return x + sum(x - 1)


n= int(input("Enter the number to find the sum: "))

def main():
    #call the function
    sum(n)
    
print(f"The sum of first {n} numbers: ",sum(n))
