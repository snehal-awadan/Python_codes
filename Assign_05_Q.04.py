# Assign: 05
# Q.04)

# function to delete dictionary keys:
def delete_dict_keys(sampleDict,keysToRemove):
    
    for key in keysToRemove:
        if key in sampleDict:
            del sampleDict[key]


sampleDict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"
}

print("The original dictionary is:",sampleDict)

keysToRemove = ["name", "salary"]


#call the function;
delete_dict_keys(sampleDict,keysToRemove)
print("Dictionary after deleting keys: ",sampleDict)

