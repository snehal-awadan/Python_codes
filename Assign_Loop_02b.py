# Assign: "Loop"
# Q.2) --> b

n = int(input("Enter the number of rows: "))

# For upper triangle pattern; 

for i in range(n-1):
    for j in range(i,n):
        print(" ",end = "")
        
    for j in range(i):
        print("*", end ="")
        
    for j in range(i+1):
        print("*",end = "")
    print()

# For lower inverted triangle pattern; 

for i in range(n):
    for j in range(i+1):
        print(" ",end = "")
    for j in range(i,n-1):
        print("*",end = "")
    for j in range(i,n):
        print("*",end = "")
    
    print()
 
