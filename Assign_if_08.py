# Assign : "if"
# Q.8)

""" Write a program to check whether the last digit of a number( entered by user ) is divisible by
3 or not """


num = int(input("Enter any number: "))

lastDigit = num % 10    #find last digit of the num;

if lastDigit % 3 ==0:
    print("The last number is divisible by 3")
else:
    print("The last number is not divisible by 3")
