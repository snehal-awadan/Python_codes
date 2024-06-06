# menudriven program:

    #create new function for factorial;

def factorial(num):
    fact = 1
    for i in range (2,num+1):
        fact = fact*i
    return fact

# create new function to check number is prime or not;

def primeNumber(num):
    for i in range (2,num):
        if num %i==0:
            return False
    return True

    # create new function to print the table of the given number;

def printTable(num):
    for i in range (1,11):
        print(f"{num} * {i}= {num*i}")

choice = 0 
while choice!=4:   
    choice = int(input("""
        1. Factorial
        2. Prime or not
        3. print table of a number
        4. Exit
        Enter your choice: """))

    # apply match case:

match choice:
    case 1:
        print("Factorial is selected")
        num = int(input("enter number to finc its factorial : "))
            # call the function;
        result = factorial(num)
        print("factorial of the given number is: ", result)
            
          
    case 2:
        print("prime or not is selected")
        num = int(input("enter number to check it is prime or not : "))
            # call the function;
        result = primeNumber(num)
        print("The number is prime "if result else "Number is not prime")
            

    case 3:
        print("Print table is selected")
        num = int(input("enter number to print the table : "))
            # call the function;
        result =  printTable(num)
        print("The table of the given number is : ", result)

        
    case 4:
            #sys.exit(0)
        print("Thank you for visiting...!")

    case others:
         print("It is the default case")
            