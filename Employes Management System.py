# EMPLOYEES MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

import json
import os
import sys

print ("============ Welcome to Employees Management System =============")

# ---------------- File Handling ----------------

def load_employees():
    if os.path.exists("employees.json"):
        with open("employees.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def save_employees():
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=5)

employees = load_employees()

if not employees:  
    employees = [
        {"Name": "Ali", "Employee ID": 101, "Department": "HR", "Position": "Manager", "Salary": 75000},
        {"Name": "Ahmed", "Employee ID": 102, "Department": "IT", "Position": "Software Engineer", "Salary": 90000},
        {"Name": "Usman", "Employee ID": 103, "Department": "Finance", "Position": "Accountant", "Salary": 65000},
        {"Name": "Hassan", "Employee ID": 104, "Department": "Marketing", "Position": "Marketing Officer", "Salary": 55000},
        {"Name": "Bilal", "Employee ID": 105, "Department": "Sales", "Position": "Sales Executive", "Salary": 60000},
        {"Name": "Hamza", "Employee ID": 106, "Department": "IT", "Position": "Network Administrator", "Salary": 80000},
        {"Name": "Ayesha", "Employee ID": 107, "Department": "HR", "Position": "HR Officer", "Salary": 58000},
        {"Name": "Fatima", "Employee ID": 108, "Department": "Finance", "Position": "Financial Analyst", "Salary": 72000},
        {"Name": "Zain", "Employee ID": 109, "Department": "Operations", "Position": "Operations Officer", "Salary": 67000},
        {"Name": "Maryam", "Employee ID": 110, "Department": "Customer Support", "Position": "Support Executive", "Salary": 50000},
        {"Name": "Saad", "Employee ID": 111, "Department": "Administration", "Position": "Office Administrator", "Salary": 62000},
        {"Name": "Noor", "Employee ID": 112, "Department": "Research", "Position": "Research Assistant", "Salary": 70000},
        {"Name": "Abdullah", "Employee ID": 113, "Department": "Finance", "Position": "Cashier", "Salary": 52000},
        {"Name": "Umer", "Employee ID": 114, "Department": "IT", "Position": "System Administrator", "Salary": 85000},
        {"Name": "Sana", "Employee ID": 115, "Department": "Marketing", "Position": "Content Writer", "Salary": 54000},
        {"Name": "Hina", "Employee ID": 116, "Department": "Sales", "Position": "Sales Manager", "Salary": 88000},
        {"Name": "Shahzaib", "Employee ID": 117, "Department": "Operations", "Position": "Supervisor", "Salary": 68000},
        {"Name": "Laiba", "Employee ID": 118, "Department": "Customer Support", "Position": "Team Lead", "Salary": 73000},
        {"Name": "Areeb", "Employee ID": 119, "Department": "Research", "Position": "Data Analyst", "Salary": 82000},
        {"Name": "Iqra", "Employee ID": 120, "Department": "Administration", "Position": "Receptionist", "Salary": 48000}
    ]
    save_employees()

# Functions of Menu:

def print_employee(employee):
    print(f"{employee['Employee ID']:<20} {employee['Name']:<20} {employee['Department']:<25} {employee['Position']:<30} {format_currency(employee['Salary']):<30} ")

def format_currency(salary):
    return f"Rs. {salary}"

def add_employee():
    try:
        employee_ID = int(input("Enter the Employee ID: "))
    except ValueError:
        print("Invalid Employee ID! Please enter a number.")
        return
    if employee_ID <= 0:
        print("Enter a valid Employee ID!")
        return

    for employee in employees:
        if employee["Employee ID"] == employee_ID:
            print("Employee ID already exists!")
            return

    Name = input("Enter the Employee name: ")
    Department = input("Enter the Department name: ")
    Position = input("Enter the Position name: ")
    try:
        salary = int(input("Enter the Salary: "))
        if salary <=0:
            print("Salary must be a positive number!")
            return
    except ValueError:
        print("Invalid Salary! Please enter a number.")
        return  

    Name = Name.strip()
    Department = Department.strip()
    Position = Position.strip()

    if Name == "":
        print("Employee Name cannot be empty!")
        return

    if Position == "":
        print("Position cannot be empty!")
        return
    
    if Department == "":
        print("Department cannot be empty!")
        return

    new_employee = {
        "Name": Name,
        "Department": Department,
        "Employee ID": employee_ID,
        "Position": Position,
        "Salary": salary
    }

    employees.append(new_employee)
    save_employees()
    print("New Employee Added Successfully!")

def remove_employee():
    try:
        search = int(input("Enter the Employee ID: "))
    except ValueError:
        print("Invalid Employee ID! Please enter a number.")
        return

    found = False
    for employee in employees:
        if employee["Employee ID"] == search:
            confirm = input(f"Are you sure you want to delete Employee {employee['Name']}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            employees.remove(employee)
            save_employees()
            print("Employee Deleted Successfully!")
            found = True
            break
    if not found:
        print("Employee Not Found!")

def update_employee():
    try:
        search = int(input("Enter the Employee ID: "))
    except ValueError:
        print("Invalid Employee ID! Please enter a number.")
        return

    found = False
    for employee in employees:
        if employee["Employee ID"] == search:
            print("="*110)
            print("Current Details:")
            print("="*110)
            print("{:<20} {:<20} {:<15} {:>18} {:>28} ".format("Employee ID", "Name", "Department", "Position", "Salary"))
            print("="*110)
            print_employee(employee)
            print("="*110)

            Name = input("Enter the new Employee name (leave blank to keep current): ")
            Department = input("Enter the new Department name (leave blank to keep current): ")
            Position = input("Enter the new Position name (leave blank to keep current): ")
            Salary_input = input("Enter the new Salary (leave blank to keep current): ")

            if Name.strip():
                employee["Name"] = Name.strip()
            if Department.strip():
                employee["Department"] = Department.strip()
            if Position.strip():
                employee["Position"] = Position.strip()
            if Salary_input.strip():
                try:
                    salary = int(Salary_input)
                    if salary <= 0:
                        print("Salary must be a positive number! Keeping current salary.")
                    else:
                        employee["Salary"] = salary
                except ValueError:
                    print("Invalid Salary! Keeping current salary.")

            save_employees()
            print("Employee Updated Successfully!")
            found = True
            break
    if not found:
        print("Employee Not Found!")

def view_employees():
    if len(employees) == 0:
        print("No employees in Company!")
        return
    employees.sort(key=lambda emp: emp["Employee ID"])
    print("="*110)
    print("{:<20} {:<20} {:<15} {:>18} {:>28} ".format("Employee ID", "Name", "Department", "Position", "Salary"))
    print("="*110)
    for employee in employees:
        print_employee(employee)
    print("="*110)

def search_employee():
    print("-"*50)
    print("Search By:")
    print("1. Search by ID")
    print("2. Search by Name")
    print("-"*50)

    try:
        search_option = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number.")
        return

    if search_option == 1:
        try:
            search = int(input("Enter the Employee ID: "))
        except ValueError:
            print("Invalid Employee ID! Please enter a number.")
            return

        found = False
        for employee in employees:
            if employee["Employee ID"] == search:
                print("="*110)
                print("{:<20} {:<20} {:<15} {:>18} {:>28} ".format("Employee ID", "Name", "Department", "Position", "Salary"))
                print("="*110)
                print_employee(employee)
                print("="*110)
                found = True
                break
        if not found:
            print("Employee Not Found!")

    elif search_option == 2:
        try:
            search_name = input("Enter the Employee Name: ").strip()
        except ValueError:
            print("Invalid Name!")
            return
        
        if search_name == "":
            print("Name cannot be empty!")
            return

        found = False
        for employee in employees:
            if search_name.lower() in employee["Name"].lower():
                print("="*110)
                print("{:<20} {:<20} {:<15} {:>18} {:>28} ".format("Employee ID", "Name", "Department", "Position", "Salary"))
                print("="*110)
                print_employee(employee)
                print("="*110)
                found = True

        if not found:
            print("Employee Not Found!")

    else:
        print("Invalid choice! Please choose 1 or 2.")

def exit_system():
    print("Good Bye!")
    print("Thanks for using Employees Management System")
    sys.exit()

while True:
    print()
    print("=============== Employee Management Menu ===============")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("0. Exit")

    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        remove_employee()
    elif choice == 0:
        exit_system()
    else:
        print("Invalid Choice! Choose between 0 to 5")

