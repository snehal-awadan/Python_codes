# Assign : "if"
# Q.4)

""" A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade. """

marks = int(input("Enter your marks: "))

if marks<25:
    print("""Sorry, You are fail, Better luck next time!.
          Grade is F""")
    
elif marks<45:
    print("Grade is E")
    
elif marks<50:
    print("Grade is D")
    
elif marks<60:
    print("Grade is C")
    
elif marks<80:
    print("""Keep it up...!
        Grade is B""")   
else:
    print("""Congratulations...!
          Grade is A""")
