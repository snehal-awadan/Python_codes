# Assignment: 05
# Q.08)

"""  Accept name and new salary for a employee, modify salary of the employee.
display appropriate message if salary modified. or if name not found.
note : the new salary should be > current salary otherwise show message wrong salary."""

sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

print(sampleDict)

def modify_salary(sampleDict, name, new_salary):
    """
    Modify the salary of an employee if found and the new salary is greater than the current salary.
    """

    
##    for emp_id,emp_info in sampleDict.items():
##        if emp_info['name'] == name:
##            if new_salary > emp_info['salary']:
##                emp_info['salary'] = new_salary
##                return True, "Salary modified successfully."
##                
##            else:
##                return False, "New salary should be greater than the current salary."
##    return False, "Employee not found."


## OR: 



    for k,v in sampleDict.items():
        if v['name'] == name:
            if new_salary > v['salary']:
                v['salary'] = new_salary
                return True, "Salary modified successfully."
                
            else:
                return False, "New salary should be greater than the current salary."
    return False, "Employee not found."





# Accept name and new salary from user
name = input("Enter employee name: ")
new_salary = int(input("Enter new salary: "))


# Modify salary and display appropriate message
success, message = modify_salary(sampleDict, name, new_salary)
print(message)


# Display the modified dictionary
print("Updated dictionary:", sampleDict)

