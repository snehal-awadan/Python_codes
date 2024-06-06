# Assign : "Loop"
# Q.1)
""" Accept 10 integers from user and print their average value on the screen """

sum = 0
for i in range(1,11):  
    num = int(input("Enter number of rows: "))
    sum = sum + num

avg = sum/10

print("The average is :" ,avg)
    
