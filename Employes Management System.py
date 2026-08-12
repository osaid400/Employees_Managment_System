# =======================================
# Employees Management System
# Author: Muhammad Abdullah Farooq
# Language: Python 3.11
# =======================================

import json
import sys
import os


if not os.path.exists("Salary_Slips"):
    os.makedirs("Salary_Slips")


class Employee:
    def __init__(self, name, employee_id, department, position, salary, password="12345"):
        self.name = name
        self.employee_id = int(employee_id)
        self.department = department
        self.position = position
        self._salary = salary
        self.password = password
        self.leaves = []

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Salary must be positive.")
        self._salary = value

    def to_dict(self):
        return {
            "Name": self.name,
            "Employee ID": self.employee_id,
            "Department": self.department,
            "Position": self.position,
            "Salary": self._salary,
            "Password": self.password,
            "Leaves": self.leaves
        }

    @classmethod
    def from_dict(cls, data):
        emp = cls(
            name=data["Name"],
            employee_id=data["Employee ID"],
            department=data["Department"],
            position=data["Position"],
            salary=data["Salary"],
            password=data.get("Password", "12345")
        )
        emp.leaves = data.get("Leaves", [])
        return emp


class EmployeeManager:
    def __init__(self, filename="data/employees.json"):
        self.hr_username = "admin"
        self.hr_password = "0000"
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
            ]
            self.save_employees()

    def load_employees(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.employees = [Employee.from_dict(emp) for emp in data]
        except FileNotFoundError:
            self.employees = []

    def save_employees(self):
        with open(self.filename, 'w') as f:
            json.dump([emp.to_dict() for emp in self.employees], f, indent=4)

    def _find_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:  
                return employee
        return None

    @staticmethod
    def format_currency(amount):
        return f"Rs. {amount:,.0f}"

    def generate_payslip(self, employee):
        filepath = os.path.join("Salary_Slips", f"payslip_{employee.employee_id}.txt")
        allowances = employee.salary * 0.10
        deductions = employee.salary * 0.05
        net_salary = employee.salary + allowances - deductions

        with open(filepath, 'w') as f:
            f.write("=========================================\n")
            f.write("          OFFICIAL COMPANY PAYSLIP       \n")
            f.write("=========================================\n")
            f.write(f"Employee Name : {employee.name}\n")
            f.write(f"Employee ID   : {employee.employee_id}\n")
            f.write(f"Department    : {employee.department}\n")
            f.write(f"Position      : {employee.position}\n")
            f.write("-----------------------------------------\n")
            f.write(f"Basic Salary  : {self.format_currency(employee.salary)}\n")
            f.write(f"Allowances    : {self.format_currency(allowances)}\n")
            f.write(f"Deductions    : {self.format_currency(deductions)}\n")
            f.write("-----------------------------------------\n")
            f.write(f"Net Pay       : {self.format_currency(net_salary)}\n")
            f.write("=========================================\n")
        
        print(f"\n[SUCCESS] Payslip saved in 'Salary_Slips/' folder as 'payslip_{employee.employee_id}.txt'!")

    def show_department_analytics(self):
        if not self.employees:
            print("No data available for analytics.")
            return

        dept_data = {}
        for emp in self.employees:
            if emp.department not in dept_data:
                dept_data[emp.department] = {"count": 0, "payroll": 0}
            dept_data[emp.department]["count"] += 1
            dept_data[emp.department]["payroll"] += emp.salary

        print("=" * 70)
        print(f"{'Department':<20} {'Total Employees':<25} {'Total Payroll':<25}")
        print("=" * 70)
        total_company_payroll = 0
        for dept, info in dept_data.items():
            print(f"{dept:<27} {info['count']:<18} {self.format_currency(info['payroll']):<25}")
            total_company_payroll += info["payroll"]
        print("=" * 70)
        print(f"Total Company Payroll across all departments: {self.format_currency(total_company_payroll)}")
        print("=" * 70)
  
    def sort_and_filter_menu(self):
        print("\n--- Sort & Filter Employees ---")
        print("1. Sort by Salary (High to Low)")
        print("2. Sort Alphabetically by Name")
        print("3. Filter by Department")
        
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            return

        if choice == 1:
            sorted_emps = sorted(self.employees, key=lambda x: x.salary, reverse=True)
            self._print_employee_table(sorted_emps)
        elif choice == 2:
            sorted_emps = sorted(self.employees, key=lambda x: x.name)
            self._print_employee_table(sorted_emps)
        elif choice == 3:
            dept = input("Enter department name to filter: ").strip()
            filtered = [emp for emp in self.employees if emp.department.lower() == dept.lower()]
            if filtered:
                self._print_employee_table(filtered)
            else:
                print(f"No employees found in department '{dept}'.")
        else:
            print("Invalid choice!")

    def _print_employee_table(self, emp_list):
        print("=" * 110)
        print(f"{'ID':<10} {'Name':<20} {'Department':<20} {'Position':<25} {'Salary':<15}")
        print("=" * 110)
        for emp in emp_list:
            print(f"{emp.employee_id:<10} {emp.name:<20} {emp.department:<20} {emp.position:<25} {self.format_currency(emp.salary):<15}")
        print("=" * 110)

    def add_employee(self):
        try:
            employee_id = int(input("Enter Employee ID: "))
        except ValueError:
            print("Invalid ID! Must be a number.")
            return

        if self._find_by_id(employee_id):
            print("Employee ID already exists!")
            return

        name = input("Enter Employee Name: ").strip()
        department = input("Enter Department: ").strip()
        position = input("Enter Position: ").strip()
        
        try:
            salary = int(input("Enter Salary: "))
            if salary <= 0:
                print("Salary must be positive.")
                return
        except ValueError:
            print("Invalid salary number.")
            return

        if not name or not department or not position:
            print("Fields cannot be empty!")
            return

        new_emp = Employee(name, employee_id, department, position, salary)
        self.employees.append(new_emp)
        self.save_employees()
        print("[SUCCESS] New Employee Added Successfully with default password '12345'!")

    def view_employees(self):
        if not self.employees:
            print("No employees available.")
            return
        self._print_employee_table(self.employees)

    def update_employee(self):
        try:
            search_id = int(input("Enter Employee ID to update: "))
        except ValueError:
            print("Invalid ID.")
            return

        emp = self._find_by_id(search_id)
        if emp:
            print("Leave blank to keep existing details:")
            emp.name = input(f"Name ({emp.name}): ") or emp.name
            emp.department = input(f"Department ({emp.department}): ") or emp.department
            emp.position = input(f"Position ({emp.position}): ") or emp.position
            new_sal = input(f"Salary ({emp.salary}): ")
            if new_sal:
                try:
                    emp.salary = int(new_sal)
                except ValueError:
                    print("Invalid salary format, keeping old value.")
            self.save_employees()
            print("[SUCCESS] Employee updated successfully!")
        else:
            print("Employee not found!")

    def remove_employee(self):
        try:
            search_id = int(input("Enter Employee ID to delete: "))
        except ValueError:
            print("Invalid ID.")
            return

        emp = self._find_by_id(search_id)
        if not emp:
            print("Employee not found!")
            return

        confirm = input(f"Are you sure you want to delete {emp.name}? (y/n): ")
        if confirm.lower() == 'y':
            self.employees.remove(emp)
            self.save_employees()
            print("[SUCCESS] Employee deleted successfully!")
        else:
            print("Deletion cancelled.")

    def show_leave_requests(self):
        print("\n--- ALL EMPLOYEE LEAVE REQUESTS ---")
        
        file_path = "data/leave_requests.json"
        leave_requests = []
        
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        leave_requests = json.loads(content)
            except Exception:
                leave_requests = []
        elif hasattr(self, 'leave_requests'):
            leave_requests = self.leave_requests

        if not leave_requests:
            print("No leave requests found.")
            print("-" * 50)
            return

        for idx, leave in enumerate(leave_requests):
            emp_id = leave.get('emp_id', leave.get('id', 'N/A'))
            name = leave.get('name', 'Unknown')
            l_type = leave.get('type', 'N/A')
            l_reason = leave.get('reason', 'No reason provided')
            l_status = leave.get('status', 'Pending')
            
            print(f"Employee ID: {emp_id} | Name: {name}")
            print(f"Leave #{idx+1} | Type: {l_type} | Reason: {l_reason} | Status: {l_status}")
            print("-" * 60)

    def search_employee_panel(self):
        print("-"*50)
        print("Search By:")
        print("1. ID")
        print("2. Name")
        print("3. Department")
        print("-"*50)
        try:
            opt = int(input("Choice: "))
        except ValueError:
            return
        
        if opt == 1:
            eid = int(input("Enter ID: "))
            emp = self._find_by_id(eid)
            if emp: self._print_employee_table([emp])
            else: print("Not found.")
        elif opt == 2:
            name = input("Enter Name: ").lower()
            res = [e for e in self.employees if name in e.name.lower()]
            if res: self._print_employee_table(res)
            else: print("Not found.")
        elif opt == 3:
            dept = input("Enter Dept: ").lower()
            res = [e for e in self.employees if dept in e.department.lower()]
            if res: self._print_employee_table(res)
            else: print("Not found.")

    def view_leave_history(self, employee):
        if not employee.leaves:
            print("No leave history found.")
            return
        print(f"\n======================== Leave History for {employee.name} ========================")
        for idx, l in enumerate(employee.leaves, 1):
            l_type = l.get('type', 'N/A')
            l_reason = l.get('reason', 'No reason provided')
            l_status = l.get('status', 'Pending')
            print(f"{idx}. Type: {l_type} | Reason: {l_reason} | Status: {l_status}")
            print("=======================================================================")

    def apply_for_leave(self, employee):
        print("\n========================== Leave Application ==========================")
        print("1. Full Day Leave")
        print("2. Half Day Leave")
        print("=======================================================================")

        leave_type_choice = input("Select type (1 or 2): ").strip()
        
        if leave_type_choice == "1":
            leave_type = "Full Day"
        elif leave_type_choice == "2":
            leave_type = "Half Day"
        else:
            print("Invalid leave type selection.")
            return
        
        reason = input("Enter Reason for Leave: ").strip()
        if not reason:
            print("Reason cannot be empty.")
            return

        print(f"\nApplying for {leave_type} Leave...")
        
        employee.leaves.append({
            "type": leave_type, 
            "reason": reason, 
            "status": "Pending"
        })
        self.save_employees()
        print("[SUCCESS] Leave application submitted successfully!")

    def view_employee_profile(self, employee):

        print("\n=========================== My Profile Details ===========================")
        print(f"Name       : {employee.name}")
        print(f"ID         : {employee.employee_id}")
        print(f"Department : {employee.department}")
        print(f"Position   : {employee.position}")
        print(f"Salary     : {self.format_currency(employee.salary)}")
        print("===========================================================================")

    def logout_employee(self, employee):
        print("Goodbye!")
        print(f"Logging out {employee.name}...")

def employee_menu(company, employee):
    while True:
        print(f"\n==================== EMPLOYEE PANEL ({employee.name}) ====================")
        print("1. View My Profile & Department Details")
        print("2. Apply for Leave (Full Day / Half Day)")
        print("3. View My Leave History & Status")
        print("4. Generate & Download My Payslip (.txt)")
        print("0. Logout")
        print("==============================================================================")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice! Enter a number.")
            continue

        if choice == 1:
            company.view_employee_profile(employee)

        elif choice == 2:
            company.apply_for_leave(employee)
            
        elif choice == 3:
            company.view_leave_history(employee)

        elif choice == 4:
            company.generate_payslip(employee)
        elif choice == 0:
            company.logout_employee(employee)
            break
        else:
            print("Invalid choice! Choose between 0 to 4.")

def admin_menu(company):
    while True:                         
        print("\n========================== ADMIN / HR MANAGEMENT PANEL ==========================")
        print("1. Add New Employee")
        print("2. View All Employees Roster")
        print("3. Search Employee (ID, Name, Dept)")
        print("4. Update Employee Details")
        print("5. Delete Employee")
        print("6. Department-Wise Payroll Analytics Dashboard")
        print("7. Sort & Filter Employees List")
        print("8. View & Approve/Reject Leave Requests")
        print("9. Generate Payslip for any Employee")
        print("0. Logout")
        print("=====================================================================================")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid Choice! Please enter a number.")
            continue

        if choice == 1:
            company.add_employee()
        elif choice == 2:
            company.view_employees()
        elif choice == 3:
            company.search_employee_panel()
        elif choice == 4:
            company.update_employee()
        elif choice == 5:
            company.remove_employee()
        elif choice == 6:
            company.show_department_analytics()
        elif choice == 7:
            company.sort_and_filter_menu()
        elif choice == 8:
            company.show_leave_requests()
        elif choice == 9:
            try:
                emp_id = int(input("Enter Employee ID to generate payslip for: "))
                emp = company._find_by_id(emp_id)
                if emp:
                    company.generate_payslip(emp)
                else:
                    print("Employee not found!")
            except ValueError:
                print("Invalid ID format.")
        elif choice == 0:
            company.logout_employee(emp)
            break
        else:
            print("Invalid Choice! Choose between 0 to 9.")


def main():
    company = EmployeeManager()

    while True:
        print()
        print("================== WELCOME TO EMPLOYEES MANAGEMENT SYSTEM =======================")
        print("\n============================ SYSTEM MENU ======================================")
        print("1. Login as HR/Admin")
        print("2. Login as Employee")
        print("0. Exit")
        print("=================================================================================")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            pwd = input("Enter Admin Password: ").strip()
            if pwd == company.hr_password:
                print("\n[SUCCESS] Logged in as Administrator (HR)!")
                admin_menu(company)
            else:
                print("\n[ERROR] Incorrect Admin Password!")
        elif choice == '2':
            try:
                eid = int(input("Enter Employee ID: "))
                pwd = input("Enter Password: ").strip()
                emp = company._find_by_id(eid)
                if emp and emp.password == pwd:
                    print(f"\n[SUCCESS] Welcome back, {emp.name}!")
                    employee_menu(company, emp)
                else:
                    print("\n[ERROR] Invalid Employee ID or Password!")
            except ValueError:
                print("\n[ERROR] Invalid Employee ID format!")

        elif choice == '0':
            print("=" * 60)
            print("Good Bye!")
            print("Thanks for using Employees Management System")
            print("=" * 60)
            sys.exit()
        else:
            print("Invalid choice! Please select 1, 2, or 0.")


if __name__ == "__main__":
    main()