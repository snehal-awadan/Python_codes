# Assign: String
# Q. 6) 

n=int(input("Enter the number: "))
def factorial(n):
    #Calculate the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(1, n+1):
    result = factorial(i)
    print(f"{i} {result}")

