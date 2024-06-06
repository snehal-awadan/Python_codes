# Assign: "String"_12
# Write a menu driven program to practice String functions;

result = ""
new_string = ""

#Display characters from even position:
def displayEvenChars(s):
   result = s[1::]   #string slicing
   return result
    

#Display characters from odd position:
def displayOddChars(s):
    result = s[::2]   #string slicing
    return result
    
#Display length of a string
def displayLength(s):
    length = len(s)
    return length


#Add 'a' at the end of string length times
def add_a(s):
    new_string = s + 'a' * len(s)
    return new_string

# take input from the user;
s = input("Enter the string:" )


#to display choice menu after every choice until choice is not 5: \
choice = 0
while choice!= 5:
        print("Enter the choice: ")
        choice = int(input("""
            1. Display characters from even position
            2. Display characters from odd position
            3. Display length of a string
            4. Add 'a' at the end of string length times
            5. Exit """ ))
        

        match choice:
                     case 1:
                         #call the function
                         print("The characters of the even number are: ",displayEvenChars(s))
                     

                     case 2:
                         # call the function
                         print("The characters of the odd number are: ",displayOddChars(s))
 
                     case 3:
                         # call the function
                         print(f"The length of the {s} is: ",displayLength(s))
                         

                     case 4:
                         # call the function
                         displayLength(s)
                         print("After adding 'a' at the end of string length times: ",add_a(s))
                         

                     case 5:
                         print("Thank You for waiting.....!")
                     
                     case _:
                         print("Invalid choice")
                     
             

