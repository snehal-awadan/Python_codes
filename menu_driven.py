# menu driven program:



def factorial(num):
    fact = 1
    for i in range(num):
        fact = fact*i
    return fact

def primeornot(num):
    for i in range(num):
        if num % i == 0:
            return False
    return True
                       
def printtable(num):
    for i in range(11):
        print(f"{num} * {i} = {num*i}")
    

choice = 0
while choice!=4:
    choice = int(input(""" 1.factorial
                            2.prime or not
                            3. print table of a number
                            4. exit.
                            enter your choice:
                            """))
    match choice:
            case 1:
                num = int(input("enter a num to find the factorial:"))
                factorial(num)

            case 2:
                num = int(input("enter a num"))
                primeornot(num)

            case 3:
                num = int(input("enter a num"))
                printtable(num)
                
            case 4:
                print("thank you")

            case _:
                print("invalid user")
                
                
        
