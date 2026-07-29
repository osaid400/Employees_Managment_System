# EMPLOYEES MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python

import json
import os
import sys

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Employee:
    def __init__(self, name, employee_id, department, position, salary):
        self.name = name
        self.employee_id = int(employee_id)
        self.department = department
        self.position = position
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def __str__(self):
        return (
            f"Employee Name: {self.name}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Department: {self.department}\n"
            f"Position: {self.position}\n"
            f"Salary:  {self.format_currency(self.salary)}\n"
            )

    def to_dict(self):
        return {
            "Name": self.name,
            "Employee ID": self.employee_id,
            "Department": self.department,
            "Position": self.position,
            "Salary": self._salary
        }

    @classmethod
    def from_dict(cls, employee_data):
        return cls(
            name=employee_data["Name"],
            employee_id=employee_data["Employee ID"],
            department=employee_data["Department"],
            position=employee_data["Position"],
            salary=employee_data["Salary"]
        )

class Employee_Manager:
    def __init__(self, filename="employees.json"):
        self.hr_username = "admin"
        self.hr_password = "12345"
        self.filename = filename
        self.employees = []
        self.load_employees()
        if not self.employees:
            self.employees = [
                Employee("Ali", 101, "HR", "Manager", 75000),
                Employee("Ahmed", 102, "IT", "Software Engineer", 90000),
                Employee("Usman", 103, "Finance", "Accountant", 65000),
                Employee("Hassan", 104, "Marketing", "Marketing Officer", 55000),
                Employee("Bilal", 105, "Sales", "Sales Executive", 60000),
                Employee("Hamza", 106, "IT", "Network Administrator", 80000),
                Employee("Ayesha", 107, "HR", "HR Officer", 58000),
                Employee("Fatima", 108, "Finance", "Financial Analyst", 72000),
                Employee("Zain", 109, "Operations", "Operations Officer", 67000),
                Employee("Maryam", 120, "Customer Support", "Support Executive", 50000),
                Employee("Saad", 111, "Administration", "Office Administrator", 62000),
                Employee("Noor", 112, "Research", "Research Assistant", 70000),
                Employee("Abdullah", 113, "Finance", "Cashier", 52000),
                Employee("Umer", 114, "IT", "System Administrator", 85000),
                Employee("Sana", 115, "Marketing", "Content Writer", 54000),
            ]
            self.save_employees()

    def login(self):
        print("Login to Employee Management System")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username == self.hr_username and password == self.hr_password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password!")
            return False

    def load_employees(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.employees = [Employee.from_dict(emp) for emp in data]
        except FileNotFoundError:
            self.employees = []

    def save_employees(self):
        with open(self.filename, 'w') as f:
            json.dump([emp.to_dict() for emp in self.employees], f, indent=5)

    def format_currency(self, salary):
        return f"Rs. {salary:,.0f}"

    def _find_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:  
                return employee
        return None

    def print_employee(self):
        print("=" * 80)
        print(f"{'Employee Name':<8} {'Employee ID':<32} {'Department':<20} {'Position':<20} {'Position':<20}")
        print("=" * 80)

    @staticmethod
    def format_currency(salary):
        return f"Rs. {salary:,.0f}"

    def calculate_payroll(self):
        print("=========================================================")
        total_payroll = sum(employee.salary for employee in self.employees)
        print(f"Total Company Payroll: {self.format_currency(total_payroll)}")
        print("=========================================================")
        
    def add_employee(self):
        try:
            employee_id = int(input("Enter the Employee ID: "))
        except ValueError:
            print("Invalid Employee ID! Please enter a number.")
            return
        if employee_id <= 0:
            print("Enter a valid Employee ID!")
            return

        if self._find_by_id(employee_id):
            print("Employee ID already exists!")
            return

        name = input("Enter the Employee name: ")
        department = input("Enter the Department name: ")
        position = input("Enter the Position name: ")

        try:
            salary = int(input("Enter the Salary: "))
            if salary <=0:
                print("Salary must be a positive number!")
                return
        except ValueError:
            print("Invalid Salary! Please enter a number.")
            return  

        name = name.strip()
        department = department.strip()
        position = position.strip()

        if name == "":
            print("Employee Name cannot be empty!")
            return

        if position == "":
            print("Position cannot be empty!")
            return
    
        if department == "":
            print("Department cannot be empty!")
            return

        new_employee = Employee(name, int(employee_id), department, position, salary)        
        self.employees.append(new_employee)
        self.save_employees() 
        print("New Employee Added Successfully!")

    def view_employees(self):
        if not self.employees:
            print("No employees available in the company!")
            return
        self.employees.sort(key=lambda b: b.employee_id)
        print("=" * 120)
        print(f"{'Employee Name':<20} {'Employee ID':<20} {'Department':<25} {'Position':<30} {'Salary':<20}")
        print("=" * 120)
        for employee in self.employees:
            print(f"{employee.name:<20} {employee.employee_id:<20} {employee.department:<25} {employee.position:<30} {Employee_Manager.format_currency(employee.salary):<20}")        
        print("=" * 120)

    def remove_employee(self):
        try:
            search = int(input("Enter the Employee ID: "))
        except ValueError:
            print("Invalid Employee ID! Please enter a number.")
            return

        found = False

        employee = self._find_by_id(search)
        confirm = input(f"Are you sure you want to delete Employee (employee['Name'])? (y/n): ")
        if confirm.lower() != "y":
            print("Deletion cancelled.")
            return
        self.employees.remove(employee)
        self.save_employees()
        print("Employee Deleted Successfully!")

        found = True
        
        if not found:
            print("Employee Not Found!")

    def update_employee(self):
        try:
            search = int(input("Enter the Employee ID: "))
        except ValueError:
            print("Invalid Employee ID! Please enter a number.")
            return
        employee = self._find_by_id(search)
        if employee:
            print("Enter new details (leave blank to keep current):")
            employee.name = input(f"Name ({employee.name}): ") or employee.name
            employee.department = input(f"Department ({employee.department}): ") or employee.department
            employee.position = input(f"Position ({employee.position}): ") or employee.position
            new_salary = input(f"Salary ({employee.salary}): ")
            if new_salary:
                try:
                    employee.salary = int(new_salary)
                except ValueError:
                    print("Invalid salary! Keeping current.")
            self.save_employees()
            print("Employee updated successfully!")
        else:
            print("Employee Not Found!")

    def search_employee(self):
        print("-"*50)
        print("Search By:")
        print("1. Search by ID")
        print("2. Search by Name")
        print("3. Search by Department")
        print("4. Search by Position")
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

            employee = self._find_by_id(search)

            if employee:
                print("="*120)
                print(f"{'Employee ID':<20} {'Name':<20} {'Department':<25} {'Position':<30} {'Salary':<20} ")
                print("="*120)
                print(f"{employee.name:<20} {employee.employee_id:<20} {employee.department:<25} {employee.position:<30} {Employee_Manager.format_currency(employee.salary):<20}")                
                print("="*120)
            else:
                print("Employee Not Found!")

        elif search_option == 2:
            search_name = input("Enter the Employee Name: ").strip()
            if search_name == "":
                print("Name cannot be empty!")
                return
            found = False
            print("="*120)
            print(f"{'Employee ID':<20} {'Name':<20} {'Department':<25} {'Position':<30} {'Salary':<20} ")
            print("="*120)
            for employee in self.employees:
                if search_name.lower() in employee.name.lower():
                    print(f"{employee.name:<20} {employee.employee_id:<20} {employee.department:<25} {employee.position:<30} {Employee_Manager.format_currency(employee.salary):<20}")                
                    print("="*120)
                    found = True
            print("="*120)
            if not found:
                print("Employee Not Found!")
        elif search_option == 3:
            search_dept = input("Enter the Department: ").strip()
            if search_dept == "":
                print("Department cannot be empty!")
                return
            found = False
            print("="*120)
            print(f"{'Employee ID':<20} {'Name':<20} {'Department':<25} {'Position':<30} {'Salary':<20} ")
            print("="*120)
            for employee in self.employees:
                if search_dept.lower() in employee.department.lower():
                    print(f"{employee.name:<20} {employee.employee_id:<20} {employee.department:<25} {employee.position:<30} {Employee_Manager.format_currency(employee.salary):<20}")                
                    print("="*120)
                    found = True
            print("="*120)
            if not found:
                print("No employees found in this department!")

        elif search_option == 4:
            search_pos = input("Enter the Position: ").strip()
            if search_pos == "":
                print("Position cannot be empty!")
                return
            found = False
            print("="*120)
            print(f"{'Employee ID':<20} {'Name':<20} {'Department':<25} {'Position':<30} {'Salary':<20} ")
            print("="*120)
            for employee in self.employees:
                if search_pos.lower() in employee.position.lower():
                    print(f"{employee.name:<20} {employee.employee_id:<20} {employee.department:<25} {employee.position:<30} {Employee_Manager.format_currency(employee.salary):<20}")                
                    print("="*120)
                    found = True
            print("="*120)
            if not found:
                print("No employees found in this position!")
        else:
            print("Invalid choice! Please choose 1, 2, 3 or 4.")

    def exit_system(self):
        print("=" * 100)
        print("Good Bye!")
        print("Thanks for using Employees Management System")
        print("=" * 100)
        sys.exit()


def main():

    print("============ Welcome to Employee Management System =============")
    company = Employee_Manager()
    if not company.login():
        return

    while True:
    
        print()
        print("=============== Employee Management Menu ===============")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Total Compnay Payroll")
        print("0. Exit")
        print("=========================================================")

        try:
            choice = int(input("Enter the number: "))
        except ValueError:
            print("Invalid Choice! Please enter a number.")
            continue
        except Exception as e:
            print(f"An error occurred: (e)")
            continue

        if choice == 1:
            company.add_employee()
        elif choice == 2:
            company.view_employees()
        elif choice == 3:
            company.search_employee()
        elif choice == 4:
            company.update_employee()
        elif choice == 5:
            company.remove_employee()
        elif choice == 6: 
            company.calculate_payroll()
        elif choice == 0:
            company.exit_system()
        else:
            print("Invalid Choice! Choose between 0 to 5")


if __name__ == "__main__":
    main()