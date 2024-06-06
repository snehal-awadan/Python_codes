# Assign "if":
# Q.1)

"""  A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""



# Create new function to calculate the percentage;
def calcPercentage(classes,attended):
    Perc = (attended/classes)*100
    return Perc

classes = int(input("Enter the total number of classes held: "))
attended = int(input("Enter the number of classes that you have attended: "))

#Call the function
result = calcPercentage(classes,attended)
print(result)

#check the condition;
if result<=75:
    print("You are not allowed for exam as your percentage is below 75%")
else:
    print("You are allowed for exam")
