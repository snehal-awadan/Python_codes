#Assign _07
#Q.04)

""" username should contain only alphabets or digits
and password length should be 8, starts with alphabet and should contain at least one special character(#,@).
accept username and password from user and validate it.
if it is valid then display message 
welcome to our application. otherwise ask to re-enter.
allows maximum 3 attempts to accept password """

import re

def modify_username(username):
    return  bool(re.match("^[a-zA-Z0-9]+$",username))
    
def modify_password(password):     
    return bool(re.match("^[a-zA-Z][a-zA-Z0-9#@$]{7}$",password))
        
attempts=3
while attempts>0:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    length = len(password)

    if modify_username(username)and modify_password(password):
        print("Welcome to our application")
    else:
        print("Invalid")
        print("enter your password again: ")
        if modify_username(username)and modify_password(password):
            print("Welcome to our application")

        attempts = -1
if attempts == 0:
    print("You have reached the maximum attempts")
            
