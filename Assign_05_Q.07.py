#Assign: 05
# Q.07)

""" display the key of a maximum value from the following dictionary """

sampleDict = {
 'Physics': 82,
 'Math': 65,
 'history': 82
}

max_key = max(sampleDict, key=lambda k: sampleDict[k])

print("Key with maximum value:", max_key)
