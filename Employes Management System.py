# EMPLOYEES MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

print ("============ Welcome to Employees Management System =============")
    
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
        salary = float(input("Enter the Salary: "))
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
            print("---------------------------------------------------")
            print("Current Details:")
            print("Name:", employee["Name"])
            print("Department:", employee["Department"])
            print("Employee ID:", employee["Employee ID"])
            print("Position:", employee["Position"])
            print("Salary:", employee["Salary"])
            print("---------------------------------------------------")

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
                    salary = float(Salary_input)
                    if salary < 0:
                        print("Salary must be a positive number! Keeping current salary.")
                    else:
                        employee["Salary"] = salary
                except ValueError:
                    print("Invalid Salary! Keeping current salary.")

            print("Employee Updated Successfully!")
            found = True
            break
    if not found:
        print("Employee Not Found!")

def view_employees():
    if len(employees) == 0:
        print("No employees in Company!")
        return
    for employee in employees:
            print("---------------------------------------------------")
            print("Name:", employee["Name"])
            print("Department:", employee["Department"])
            print("Employee ID:", employee["Employee ID"])
            print("Position:", employee["Position"])
            print("Salary:", employee["Salary"])
            print("---------------------------------------------------")

def search_employee():
    try:
        search = int(input("Enter the Employee ID: "))
    except ValueError:
        print("Invalid Employee ID! Please enter a number.")
        return

    found = False
    for employee in employees:
        if employee["Employee ID"] == search:
            print("---------------------------------------------------")
            print("Name:", employee["Name"])
            print("Department:", employee["Department"])
            print("Employee ID:", employee["Employee ID"])
            print("Position:", employee["Position"])
            print("Salary:", employee["Salary"])
            print("---------------------------------------------------")
            found = True
            break
    if not found:
        print("Employee Not Found!")

def exit_system():
    print("Good Bye!")
    print("Thanks for using Employees Management System")
    exit()

while True:
    print()
    print("=============== Select the Option (0-5) ===============")
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
        break
    else:
        print("Invalid Choice! Choose between 0 to 5")

