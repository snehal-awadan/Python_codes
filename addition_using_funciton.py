# Accept two numbers from user and perform Addition using Function.

#create new function for addition;
def addition(num1,num2):
    add = num1 + num2;
    return add

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#call function:

result = addition(num1, num2)
print(" Addition is: ",result)
