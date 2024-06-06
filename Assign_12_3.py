# Assign: 12
# Q.3) List Menu driven program

""" Write a menu driven program to practice List functions. """

#Accept data:
def acceptData(data):
    if add_data == 1:
        result = list.append(data)
        return result
    else:
        result = list.insert(pos,data)

#Delete data by value;
def deleteData(data): 
        if data in list: 
            result = list.remove(data)
            print(f"{data} is deleted successfully..")
            return result
        else:
            print(f"{data} is not found in list")

# Delete data by position;
def delete_data_position(pos):
        for i in range(len(list)):
            if i == pos:
                result = list.pop(pos)
        return result

#sort:
def sorted_list(sort_list):
    if sort_list == 1:
        result = list.sort()
        return result

def sorted_list_descending(sorted_list):
    if sort_list == 2:
        result = sorted(list,reverse= True)
        return result

# Reverse:
def reverse_list(list):
    new_list = list[::-1]
    return new_list

# Print in sorted order without changing original list
def sorted_order(list):
    list1 = sorted(list)
    return list1

    
# print in reverse order without changing original list

def reverse_original_list(list):
    list1 = sorted(list,reverse = True)
    return list1


# Display data:
def displayAll(list,format):
    if format == 1:
        print("Normal list: ",list)
    else:
        print("Numbered list: ")
        for i, data in enumerate(list,start =1):
            print(f"{i}. {data}")      



list = [90,50,80,10,20,30,40]
print("The list is: ",list)

choice = 0
while choice!= 10:
    
    print("""
            1. Accept data
            2. Delete data by value
            3. Delete data by position
            4. Sort
            5. Reverse
            6. Print in sorted order without changing original list
            7. Print in reverse order without changing original list
            8. Display data
            9. Exit """)
    
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
                print("""
                          1. add at last position
                          2. add at given position """ )
                
                add_data = int(input("Enter your choice to add the data: "))
                data = int(input("Enter the data to add into the list: "))

                if add_data == 1:
                    #call the function
                    result = acceptData(data)
                    print(f"After adding the {data} into the list: ",list)
                else:
                    pos = int(input(f"Enter the position to add {data} :"))
                    result = acceptData(data)
                    print(f"After adding the {data} at {pos} into the list: ",list)

        case 2:
               data = int(input("Enter the data to delete it: "))
               # call the function
               result = deleteData(data)
               print(list)

        case 3:
                print("""
                        1. Delete last element
                        2. Delete from particular position""")
                
                delete_data = int(input("Enter your choice: "))
                if delete_data == 1:
                    result = list.pop()
                    print(f"After deleting the last element: ",list)
                else:
                    pos = int(input("Enter the position to delete: "))
                    # call the function
                    result = delete_data_position(pos)
                    print(f"After deleting the {pos} index: ",list)
                            
        case 4:
                print("""
                        1. Sorting in ascending order
                        2. Sorting in descending order""")
                sort_list = int(input("Enter your choice: "))
                if sort_list ==1:
                    #call function;
                    result = sorted_list(sort_list)
                    print("After sorting the list in ascending order: ",list)
                else:
                    result = sorted_list_descending(sorted_list)
                    print("After sorting the listin descending order: ",list)
                                      
        case 5:
                 #call the function
                 result = reverse_list(list)
                 print("After revversing the list: ",result)
           
        case 6:
                print("The original list: ",list)
                #call the function
                result = sorted_order(list)
                print("The list in sorted order",result)

        case 7:
                print("The original list: ",list)
                #call the function
                result = reverse_original_list(list)
                print("The list in revered order",result)
        case 8:
                format = int(input("""Enter your choice :
                                   1. Normal
                                   2. Numbered """))
                #call the function
                result = displayAll(list,format)


        case 9:
                print("Thank you for visiting...! ")

        case _:
                print("You have entered invalid choice...")

        
                    


