# Q.07)

def generate_list_of_lists(num):
    # Initialize an empty list to hold the list of lists
    result_lists = [[] for _ in range(10)]

    # Get the last digit of the number
    last_digit = num % 10

    # Add the number to the appropriate position in the list of lists
    result_lists[last_digit].append(num)

    return result_lists

# Accept a number from the user
number = int(input("Enter a number: "))

# Generate the list of lists based on the number
result = generate_list_of_lists(number)

print("Resulting list of lists:", result)


"""" incomplete""""
