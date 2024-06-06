# Assign : "String"
# Q.4)
""" write a function to check a sentence to see if it is a pangram or not."""


import string
s = input("Enter the string to check if it is pangram or not: ")

#create function for pangram;
def isPangram(s):
    
    # string.ascii_lowercase :It is a constant provided by the string module in Python,
    #which contains all the lowercase letters of the English alphabet as a single string
    
    result = set(string.ascii_lowercase)
    return set(s.lower()) >= result

if isPangram(s):
    
    print("The given string is pangram")
else:
    print("The given string is not pangram")
