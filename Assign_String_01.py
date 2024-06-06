#Assign: "String"
# Q.01)

""" Write a program that asks the user how many days are in a month,
and what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc),
and then prints a calendar for that month.
accept number of days in a month, 29,28,30,31
when the month starts (mon-0,tue-1)

"""

while True:
    numdays=int(input("Enter days of the months: "))
    if numdays>=28 and numdays<=31:
        break
    
while True:
    startday=int(input(""" 0-monday 1-tuesday 2-wednesday 3-thursday 4-friday 5-saturday 6-sunday
    When month is going to start:"""))
    
    if startday>=0 and startday<=6:
        break
    
print("Mon\t Tue\t Wed\t Thu\t Fri\t sat\t sun")

#it will print spaces before 1, useful only for line 1
print("   \t"*startday,end="")

count=startday

for i in range(1,numdays+1):
    print(" "+str(i),end="\t")
    count=count+1
    
    #to bring the cursor on the next line
    if count==7:
        print()
        count=0
