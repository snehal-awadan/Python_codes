 # Assign: "If"
 # Q.7)
 
""" Write a program to calculate the electricity bill """

unit = int(input("Enter the unit of the electricity: "))
if unit <= 100 :
    print("No charge")
else :
    unit = unit - 200
    bill = 500
    if unit > 0 :
        bill = bill + (unit * 10)
    print("Bill : ",bill)
