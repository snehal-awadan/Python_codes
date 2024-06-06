#Assign: 05
# Q.05)
""" display all the keys with value 200 from the following dictionary."""


sampleDict = {'a': 100, 'b': 200, 'c': 300, "d":200}
print(sampleDict)
for k,v in sampleDict.items():
    if v == 200:
        print(k)

