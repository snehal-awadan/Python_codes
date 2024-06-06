# Assign: "if"
# Q.9)
""" Write a program to check whether an years is leap year or not """


year=int(input("Enter a year:"))

if year %100 == 0:
    if year %400 == 0:
        print("It is leap year.")

if year % 4 == 0 and year % 100!=0:
    print("It is leap year.")
else:
    print("It is not leap year.")




