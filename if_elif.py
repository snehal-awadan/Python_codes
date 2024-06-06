a=int(input("Enter any int number:"))

if a<=10:
    a = a+100
elif a<30:
    a = a+200
elif a>=30:
    a = a+400
else:
    a = a+600
print(a)

#it will print * and space 50 times using *(multiiplacation) sign (instead of using for loop)
print("* " *50)

# Walrus Operator: it first assigns the value to the variable then checks the given condition;
if a:=2<5:
    print("a is smaller")
else:
    print("a is greater")