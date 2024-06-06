# Assign : "if"
#Q. 6)

""" Accept number from user and check whether it is divisible by 5 and 11
if divisible then display appropriate message.
 """


# create the function to check: if the num is divisible by 5
def isdivisibleby5(num):
    if num%5 == 0:
        print("No is divisible by 5")
    else:
        print("No is not divisible by 5")            
        return 1

# create the function to check: if the num is divisible by 11
def isdivisibleby11(num):
    if num%11 == 0:
        print("No is divisible by 11")
    else:
        print("No is not divisible by 5")
        return 1

num=int(input("enter a number:"))

#call the functions:
isdivisibleby5(num)
isdivisibleby11(num)

