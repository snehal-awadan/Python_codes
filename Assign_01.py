# Assign: 15
# Q, 1)
# regular expression

import re

def matchExpression(lines):
    result = {"found": [], "Not found": []}

    pattern = re.compile(".*m(?:id)?$")

    for line in lines:
        match = re.match(pattern,line)
        if match:
            result["found"].append(line)
        else:
            result["Not found"].append(line)
    return result

lines = []
print("Enter lines (type 'q' to exit): ")
while True:
    line = input("Enter sentence: ")
    if line.lower() == "q":
        break
    lines.append(line)

# stored in dict;
result_dict = matchExpression(lines)
print(result_dict)
