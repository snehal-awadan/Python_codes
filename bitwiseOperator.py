# Bitwise opearator:
a=11
b=9

print(a)
print(b)

print("converting int to binary: ")
print("a",bin(a))
print("b",bin(b))

# apply left shift-> doubled the number
d = b<<4
print(d)
result = d|a    # OR opearation
print(result, "->", bin(result))

# To separate them:
print("mask", int(0b01111))
a1 = result & 15 
print(a1)

# Get the original value of b:
b1 = result>>4      # right shift -> half the number.
print(b1)
