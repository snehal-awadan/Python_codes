# Assign: "List"
# Q.08)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)
print(list1)



##list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
##print(list)
##
##lst = list1[2][1][2]
##lst.extend(["h","i","j"])
##print(list1)
