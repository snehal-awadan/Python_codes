# Assign "if":
# Q.3)
""" Modify the above question to allow student to sit if he/she has medical cause. Ask
user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly. """

# create new function to calculate percentage:
def calcPercentage(a,b):
    Perc = (b/a)*100
    return Perc

classes = int(input("Enter the total number of classes held: "))
attended = int(input("Enter the number of classes that you have attended: "))

#Call the function
result = calcPercentage(classes,attended)
print("Percentage is: ", result)

#check the condition;

if result<=75:
    medical = input("Is there any medical cause? Y/N : ")
    if medical == "Y":
        print("You are allowed in exam. Just submit your medical report to exam section")
    else:
        print("You are not allowed in exam.") 
else:
    print("You are allowed in exam.")
