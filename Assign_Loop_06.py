# Assign :"List"
# Q. 06)

list1 = ["Ashish","","Atharva","Amit","","Revati"]

for ch in list1:
    if ch == "":
        list1.remove(ch)
print(list1)
