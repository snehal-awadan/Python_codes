strings = ["apple", "banana", "cherry", "date"]

# Find the string with the maximum value when sorted in reverse order
last_string = max(strings, key=lambda x: x[::-1])

print("String with maximum length:", last_string)


strings = ["apple", "banana", "orange"]

# Find the last string after reversing each string
last_string = max(strings, key=lambda x: x[::-1])

print("Last string after reversing:", last_string)


string = "example"
last_element = (lambda x: x[-1])(string[::-1])
print(last_element)


