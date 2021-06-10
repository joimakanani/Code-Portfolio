#****************************************************************************************************
#
#       Name:          Joi Wilson
#       Course:        COSC 2110 Computer Languages: Python
#       Assignment:    employees.py
#       Due Date:      10/16/2020
#       Description:
#               Write a program that organizes a menu to add, account and delete
#               employees in the system
#
#****************************************************************************************************

import pickle
from employee import Employee

outfile = 'employee.dat'
LOOK = 1
ADDING = 2
CHANGING = 3
DELETING = 4
QUITTING = 5


# ****************************************************************************************************
def load_employees():
    try:
        fp = open(outfile, "rb")
        emp = pickle.load(fp)
        fp.close()
    except IOError:
        emp = {}

    return emp


# ****************************************************************************************************
def get_user_choice():
    print("Menu")
    print("-" * 50)
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")

    choice = int(input("Enter your choice: "))

    while choice < LOOK or choice > QUITTING:
        print("Invalid choice")
        choice = int(input("Enter your choice: "))

    return choice


# ****************************************************************************************************
def look_up(employee_dict):
    id = input("Enter an employee ID number: ")
    if id in employee_dict:
        emp = employee_dict[id]
        print('Name: {}\nID number: {} \nDepartment: {}\nTitle: {}'.format(emp.get_name(), emp.get_id(),
                                                                           emp.get_department(), emp.get_job_title()))
    else:
        print("The specified ID number was not found")


# ****************************************************************************************************
def add(employee_dict):
    name = input("Enter employee name: ")
    id = input("Enter employee ID number: ")
    department = input("Enter employee department: ")
    title = input("Enter employee title: ")

    if id in employee_dict:
        print("An employee with that ID already exists.")
    else:
        employee_dict[id] = Employee(id, name, department, title)
        print("The new employee has been added.")


# ****************************************************************************************************
def change(employee_dict):
    id = input("Enter employee ID number: ")

    if id not in employee_dict:
        print("The specified ID number was not found. ")
    else:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        title = input("Enter the new title: ")
        employee_dict[id].set_name(name)
        employee_dict[id].set_department(department)
        employee_dict[id].set_job_title(title)
        print("Employee information updated.")


# ****************************************************************************************************
def delete(employee_dict):
    id = input("Enter employee ID number: ")

    if id in employee_dict:
        del employee_dict[id]
        print("Employee information deleted.")
    else:
        print("The specified ID number was not found")


# ****************************************************************************************************
def save_employee(employee_dict):
    fp = open(outfile, "wb")
    pickle.dump(employee_dict, fp)
    fp.close()


# ****************************************************************************************************
def main():
    """
    # create an employee dictionary with given records and output to the file (to create the file for the first time then you can remove the code)
    employee_dict = {"47899" : Employee("47899", "Susan Meyers", "Accounting", "Vice President"), "39119": Employee("39119", "Mark Jones", "IT", "Programmer"), \
    "81774" : Employee("81774", "Joy Rogers", "Manufacturing", "Engineer")}

    save_employee(employee_dict)
    """

    employee_dict = load_employees()
    choice = get_user_choice()

    while choice != QUITTING:
        if choice == LOOK:
            look_up(employee_dict)
        elif choice == ADDING:
            add(employee_dict)
        elif choice == CHANGING:
            change(employee_dict)
        elif choice == DELETING:
            delete(employee_dict)
        print()
        choice = get_user_choice()
    save_employee(employee_dict)


main()
