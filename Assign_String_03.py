# Assign: "String"
# Q. 3)
"""   Write a version of a palindrome recognizer that also accepts phrase palindromes. """


s = input("Enter the phrase to check if is palindrome or not: ")

# create one function for palindrome;
def isPallindrome(s):
    
    #convert given string into lowercase and remove the spaces
    s = s.replace(" ","").lower()
        
    # check if the origianl string and reverse string is same; and return it
    return s == s[::-1]

if isPallindrome(s):
    print("Yes.. it is palindrome")
else:
    print("No. it is  not palindrome")

