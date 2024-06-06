#Assign: 05
# Q.06)


""" Rename key city to location in the following dictionary """

d = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"
}
print(d)

#first remove it
d.popitem()

#append it
d["country"] = "New York"
print(d)

