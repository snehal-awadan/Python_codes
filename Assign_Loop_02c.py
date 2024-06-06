
# Assign: "Loop"
# Q.2) --> c

n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1) + "10"*(n-i) + "1", end =" ")
    print()
