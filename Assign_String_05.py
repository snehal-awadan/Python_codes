# Assign: "String"
# Q. 5)


"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
language").
That is, double every consonant and place an occurrence of "o" in between. """

s = input("Enter any string:")
vowels = "AEIOUaeiou"
result = ""

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            result = result + ch 
        else:
            result = result + ch + "o" + ch
    else:
        result = result + ch
print("The final output is: ",result)
