# assign : "if"
#Q.10)

""" Write a program to accept the price of a bike and display the road tax and
insurance to be paid according to the following criteria . also display total amount to
be paid. """

# create new function to calculate total amount;
def totalAmt(tax,insurance):
    amt= price+tax+insurance
    return amt

price=int(input("Enter your bike price: "))

if price<=50000:
    tax=price*(5/100)
    print("tax",tax)
    
    insurance=price*(5/100)
    print("insurance",insurance)
    
    #call the function;
    amt=totalAmt(tax,insurance)
    print("Total amount:",amt)
    
    
elif price<=100000:
    tax=price*(10/100)
    print("tax",tax)
    
    insurance=price*(8/100)
    print("insurance",insurance)
    
    #call the function;
    amt=totalAmt(tax,insurance)
    print("Total amount:",amt)
else:
    tax=price*(15/100)
    print("tax",tax)
    
    insurance=price*(20/100)
    print("insurance",insurance)
    
    #call the function;
    amt=totalAmt(tax,insurance)
    print("Total amount:",amt)
