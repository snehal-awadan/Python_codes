# Assign: "if"
# Q.2)

"""  accept amount from user and find the minimum number notes required to get the amount
 Notes: 2000,500,100,50,10,5,2,1   """


amount = int(input("Enter amount: "))

if amount >= 2000 : 
    count = amount // 2000
    print("2000 notes : ", count)
    amount = amount % 2000
    count = 0
    
if amount >= 500 :
    count = amount // 500
    print("500 notes: ", count)
    amount = amount % 500
    count = 0
    
if amount >= 100 : 
    count = amount // 100
    print("100 notes: ", count)
    amount = amount % 100
    count = 0
    
if amount >= 50 :
    count = amount // 50
    print("50 notes: ", count)
    amount = amount % 50
    count = 0
    
if amount >= 10 : 
    count = amount // 10
    print("10 notes: ", count)
    amount = amount % 10
    count = 0
    
if amount >= 5 : 
    count = amount // 5
    print("5 coins: ", count)
    amonunt = amount % 5
    count = 0
    
if amount >= 2 :
    count = amount//2
    print("2 coins: ", count)
    amount = amount%2
    count = 0
    
if amount >= 1 :
    count = amount // 1
    print("1 coin: ", count)
    amount = amount % 1
