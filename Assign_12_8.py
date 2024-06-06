# Assign: 12
# Q.08)

"""  Create a list to store strings in a list in following manner list
[dxz,axz,bat,rat,cat,pat,bbc,bbm,cbm,....] pat axz
 """

def add_string_to_list(string, list_dict):
    second_char = string[1]  # Get the second character of the string
    if second_char in list_dict:
        list_dict[second_char].append(string)
    else:
        list_dict[second_char] = [string]

def display_list(list_dict):
    result = []
    for key in sorted(list_dict.keys()):  # Sort keys for consistency
        result.extend(list_dict[key])
    return result




# Initialize the dictionary to store lists
list_dict = {}

input_strings = ['dxz', 'axz', 'bat', 'rat', 'cat', 'pat', 'bbc', 'bbm', 'cbm']

# Add input strings to the list_dict
for string in input_strings:
    add_string_to_list(string, list_dict)

# Display the initial list
print("Initial list:", display_list(list_dict))

# User adds 'sat'
add_string_to_list('sat', list_dict)
print("List after adding 'sat':", display_list(list_dict))

#User adds 'pick'
add_string_to_list('pick', list_dict)
print("List after adding 'pick':", display_list(list_dict))
