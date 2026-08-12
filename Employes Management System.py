# =======================================
# Employees Management System
# Author: Muhammad Abdullah Farooq
# Language: Python 3.11
# =======================================

import json
import sys
import os
import hashlib
from datetime import datetime

def _hash_pwd(password):
    return hashlib.sha256(password.encode()).hexdigest()

class Employee:
    def __init__(self, name, employee_id, department, position, salary, password="12345", leaves=None, is_frozen=False):
        self.name = name
        self.employee_id = int(employee_id)
        self.department = department
        self.position = position
        self._salary = salary
        self.password = password if len(password) == 64 else _hash_pwd(password)
        self.leaves = leaves if leaves is not None else []
        self.is_frozen = is_frozen

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
            "Leaves": self.leaves,
            "Is_Frozen": self.is_frozen
        }

    @classmethod
    def from_dict(cls, data):
        emp = cls(
            name=data.get("Name", "Unknown"),
            employee_id=data.get("Employee ID", 0),
            department=data.get("Department", "General"),
            position=data.get("Position", "Staff"),
            salary=data.get("Salary", 0),
            password=data.get("Password", _hash_pwd("12345")),
            leaves=data.get("Leaves", []),
            is_frozen=data.get("Is_Frozen", False)
        )
        return emp

class EmployeeManager:
    def __init__(self, filename="data/employees.json"):
        self.hr_username = "admin"
        self.hr_password_hash = _hash_pwd("0000")
        self.filename = filename
        self.employees = []
        self.load_employees()
        
        if not self.employees:
            self.employees = [
                Employee("Ali", 101, "HR", "Manager", 75000, _hash_pwd("12345")),
                Employee("Ahmed", 102, "IT", "Software Engineer", 90000, _hash_pwd("12345")),
                Employee("Usman", 103, "Finance", "Accountant", 65000, _hash_pwd("12345")),
                Employee("Hassan", 104, "Marketing", "Marketing Officer", 55000, _hash_pwd("12345")),
                Employee("Bilal", 105, "Sales", "Sales Executive", 60000, _hash_pwd("12345")),
                Employee("Zainab", 106, "IT", "UI/UX Designer", 70000, _hash_pwd("12345")),
                Employee("Hamza", 107, "Finance", "Financial Analyst", 80000, _hash_pwd("12345")),
                Employee("Ayesha", 108, "HR", "Recruiter", 50000, _hash_pwd("12345")),
                Employee("Omer", 109, "Operations", "Operations Manager", 85000, _hash_pwd("12345")),
                Employee("Fatima", 110, "Marketing", "Content Writer", 48000, _hash_pwd("12345")),
                Employee("Saad", 111, "IT", "Backend Developer", 95000, _hash_pwd("12345")),
                Employee("Sana", 112, "Sales", "Sales Manager", 88000, _hash_pwd("12345")),
                Employee("Zeeshan", 113, "Operations", "Logistics Officer", 52000, _hash_pwd("12345")),
                Employee("Hira", 114, "Finance", "Auditor", 72000, _hash_pwd("12345")),
                Employee("Danish", 115, "IT", "QA Engineer", 65000, _hash_pwd("12345")),
            ]
            self.save_employees()

    def load_employees(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    self.employees = []
                    return
                data = json.loads(content)
                self.employees = [Employee.from_dict(emp) for emp in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.employees = []

    def save_employees(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([emp.to_dict() for emp in self.employees], f, indent=4)

    def _load_leave_requests(self):
        file_path = "data/leave_requests.json"
        if not os.path.exists(file_path):
            return []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_leave_requests(self, requests):
        os.makedirs("data", exist_ok=True)
        file_path = "data/leave_requests.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(requests, f, indent=4)

    def _find_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:  
                return employee
        return None

    @staticmethod
    def format_currency(amount):
        return f"Rs. {amount:,.0f}"

    def generate_payslip(self, employee):
        if not os.path.exists("Salary_Slips"):
            os.makedirs("Salary_Slips")

        basic_salary = employee.salary
        
        allowance = basic_salary * 0.05
        medical = basic_salary * 0.05
        gross_salary = basic_salary + allowance + medical
        
        income_tax = basic_salary * 0.05
        
        requests = self._load_leave_requests()
        emp_approved_leaves = [
            r for r in requests 
            if r.get('emp_id') == employee.employee_id and r.get('status') == 'Approved'
        ]
        
        leave_days_count = 0.0
        for leave in emp_approved_leaves:
            l_type = leave.get('type', '')
            if l_type == 'Full Day':
                leave_days_count += 1.0
            elif l_type == 'Half Day':
                leave_days_count += 0.5
                
        per_day_salary = basic_salary / 30 if basic_salary > 0 else 0
        leave_deduction = per_day_salary * leave_days_count
        
        total_deductions = income_tax + leave_deduction
        net_salary = gross_salary - total_deductions
        
        current_date = datetime.now()
        month_year_str = current_date.strftime("%B_%Y")
        filename = f"payslip_{employee.employee_id}_{month_year_str}.txt"
        filepath = os.path.join("Salary_Slips", filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=====================================================\n")
            f.write("                 OFFICIAL COMPANY PAYSLIP            \n")
            f.write(f"                 Month: {current_date.strftime('%B %Y')} \n")
            f.write("=====================================================\n")
            f.write(f"Employee Name : {employee.name}\n")
            f.write(f"Employee ID   : {employee.employee_id}\n")
            f.write(f"Department    : {employee.department}\n")
            f.write(f"Position      : {employee.position}\n")
            f.write("-----------------------------------------------------\n")
            f.write(f"Basic Salary  : {self.format_currency(basic_salary)}\n")
            f.write(f"Allowance (5%): {self.format_currency(allowance)}\n")
            f.write(f"Medical (5%)  : {self.format_currency(medical)}\n")
            f.write(f"Gross Salary  : {self.format_currency(gross_salary)}\n")
            f.write("-------------------------------------------------------\n")
            f.write(f"Income Tax (5%): {self.format_currency(income_tax)}\n")
            f.write(f"Approved Leaves: {leave_days_count} day(s)\n")
            f.write(f"Leave Deduction: {self.format_currency(leave_deduction)}\n")
            f.write(f"Total Deductions: {self.format_currency(total_deductions)}\n")
            f.write("-------------------------------------------------------\n")
            f.write(f"Net Pay       : {self.format_currency(net_salary)}\n")
            f.write("======================================================-\n")
        
        print(f"\n[SUCCESS] Payslip saved in 'Salary_Slips/' folder as '{filename}'!")

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
        print("=" * 115)
        print(f"{'ID':<10} {'Name':<20} {'Department':<20} {'Position':<25} {'Salary':<15} {'Status':<15}")
        print("=" * 115)
        for emp in emp_list:
            status_str = "Frozen" if emp.is_frozen else "Active"
            print(f"{emp.employee_id:<10} {emp.name:<20} {emp.department:<20} {emp.position:<25} {self.format_currency(emp.salary):<15} {status_str:<15}")
        print("=" * 115)

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

        new_emp = Employee(name, employee_id, department, position, salary, _hash_pwd("12345"))
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
            name_in = input(f"Name ({emp.name}): ").strip()
            if name_in:
                emp.name = name_in
            dept_in = input(f"Department ({emp.department}): ").strip()
            if dept_in:
                emp.department = dept_in
            pos_in = input(f"Position ({emp.position}): ").strip()
            if pos_in:
                emp.position = pos_in
            new_sal = input(f"Salary ({emp.salary}): ").strip()
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

        confirm = input(f"Are you sure you want to delete {emp.name}? (y/n): ").strip()
        if confirm.lower() == 'y':
            self.employees.remove(emp)
            self.save_employees()
            print("[SUCCESS] Employee deleted successfully!")
        else:
            print("Deletion cancelled.")

    def unfreeze_employee(self):
        frozen_emps = [e for e in self.employees if e.is_frozen]
        if not frozen_emps:
            print("\n[INFO] No frozen employee accounts found.")
            return
        
        print("\n========================= FROZEN EMPLOYEE ACCOUNTS =========================")
        print(f"{'No.':<5} {'Emp ID':<10} {'Name':<20} {'Department':<20}")
        print("=" * 60)
        for idx, emp in enumerate(frozen_emps, 1):
            print(f"{idx:<5} {emp.employee_id:<10} {emp.name:<20} {emp.department:<20}")
        print("=" * 60)
        
        try:
            choice = int(input("Enter number of employee to unfreeze (0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(frozen_emps):
                target_emp = frozen_emps[choice - 1]
                target_emp.is_frozen = False
                self.save_employees()
                print(f"\n[SUCCESS] Employee {target_emp.name} (ID: {target_emp.employee_id}) account has been unfrozen successfully!")
            else:
                print("[ERROR] Invalid selection.")
        except ValueError:
            print("[ERROR] Invalid input format.")

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
        
        while True:
            date_input = input("Enter Leave Date (DD-MM-YYYY): ").strip()
            if not date_input:
                print("Date cannot be empty.")
                continue
            
            try:
                leave_date = datetime.strptime(date_input, "%d-%m-%Y").date()
                today = datetime.now().date()
                if leave_date <= today:
                    print("[ERROR] Leave date must be in the future! You cannot apply for past or current dates.")
                    continue
                break
            except ValueError:
                print("[ERROR] Invalid date format or invalid date! Please use DD-MM-YYYY (e.g., 25-08-2026).")

        reason = input("Enter Reason for Leave: ").strip()
        if not reason:
            print("Reason cannot be empty.")
            return

        print(f"\nApplying for {leave_type} Leave on {date_input}...")
        
        requests = self._load_leave_requests()
        leave_id = f"L_{int(datetime.now().timestamp() * 1000)}"
        new_request = {
            "leave_id": leave_id,
            "emp_id": employee.employee_id,
            "name": employee.name,
            "type": leave_type,
            "date": date_input,
            "reason": reason,
            "status": "Pending"
        }
        requests.append(new_request)
        self._save_leave_requests(requests)
        
        print("[SUCCESS] Leave application submitted successfully!")

    def show_leave_requests(self):
        while True:
            print("\n========================= PENDING LEAVE REQUESTS =========================")
            requests = self._load_leave_requests()

            pending_requests = [r for r in requests if r.get('status', 'Pending') == 'Pending']

            if not pending_requests:
                print("No pending leave requests found.")
                print("=" * 73)
                return

            print(f"{'No.':<5} {'Emp ID':<10} {'Name':<15} {'Type':<12} {'Date':<15} {'Status'}")
            print("=" * 73)
            for idx, req in enumerate(pending_requests, 1):
                emp_id = str(req.get('emp_id', 'N/A'))
                name = req.get('name', 'Unknown')
                l_type = req.get('type', 'N/A')
                l_date = req.get('date', 'N/A')
                l_status = req.get('status', 'Pending')
                
                print(f"{idx:<5} {emp_id:<10} {name:<15} {l_type:<12} {l_date:<15} {l_status}")
            print("=" * 73)
            
            print("\nOptions:")
            print("1. Take Action (Approve / Reject a Leave Request)")
            print("0. Back to Admin Menu")
            
            choice = input("Enter choice: ").strip()
            if choice == '1':
                try:
                    req_num = int(input("Enter Leave Request Number to process: "))
                    if req_num < 1 or req_num > len(pending_requests):
                        print("[ERROR] Invalid request number!")
                        continue
                    
                    target_req = pending_requests[req_num - 1]
                    print(f"\nSelected: Leave for {target_req.get('name')} on {target_req.get('date')} | Reason: {target_req.get('reason')}")
                    print("1. Approve")
                    print("2. Reject")
                    action = input("Select action (1/2): ").strip()

                    new_status = ""
                    if action == '1':
                        new_status = 'Approved'
                    elif action == '2':
                        new_status = 'Rejected'
                    else:
                        print("[ERROR] Invalid action choice.")
                        continue

                    target_leave_id = target_req.get("leave_id")
                    for main_req in requests:
                        if target_leave_id and main_req.get("leave_id") == target_leave_id:
                            main_req['status'] = new_status
                            break
                        elif not target_leave_id and (
                            main_req.get('emp_id') == target_req.get('emp_id') and 
                            main_req.get('date') == target_req.get('date') and 
                            main_req.get('reason') == target_req.get('reason')
                        ):
                            main_req['status'] = new_status
                            break

                    self._save_leave_requests(requests)
                    print(f"[SUCCESS] Leave request {new_status.lower()} successfully!")
                except ValueError:
                    print("[ERROR] Please enter a valid number.")
            elif choice == '0':
                break
            else:
                print("[ERROR] Invalid choice! Please select 1 or 0.")

    def view_leave_history(self, employee):
        requests = self._load_leave_requests()
        emp_requests = [r for r in requests if r.get('emp_id') == employee.employee_id]

        if not emp_requests:
            print("\nNo leave history found.")
            return
            
        print(f"\n======================== Leave History for {employee.name} ========================")
        for idx, l in enumerate(emp_requests, 1):
            l_type = l.get('type', 'N/A')
            l_date = l.get('date', 'N/A')
            l_reason = l.get('reason', 'No reason provided')
            l_status = l.get('status', 'Pending')
            
            print(f"Leave Request #{idx}")
            print(f"  • Type   : {l_type}")
            print(f"  • Date   : {l_date}")
            print(f"  • Reason : {l_reason}")
            print(f"  • Status : {l_status}")
            print("-" * 65)

    def view_all_leave_history(self):
        print("\n=========================== ALL LEAVE HISTORY LOGS ==========================")
        requests = self._load_leave_requests()

        if not requests:
            print("No leave history records found.")
            print("=" * 77)
            return

        print(f"{'No.':<5} {'Emp ID':<10} {'Name':<15} {'Type':<12} {'Date':<15} {'Status'}")
        print("=" * 77)
        for idx, req in enumerate(requests, 1):
            emp_id = str(req.get('emp_id', 'N/A'))
            name = req.get('name', 'Unknown')
            l_type = req.get('type', 'N/A')
            l_date = req.get('date', 'N/A')
            l_status = req.get('status', 'Pending')
            
            print(f"{idx:<5} {emp_id:<10} {name:<15} {l_type:<12} {l_date:<15} {l_status}")
        print("=" * 77)

    def change_password(self, employee):
        print("\n--- Change Password ---")
        old_pwd = input("Enter current password: ").strip()
        if _hash_pwd(old_pwd) != employee.password:
            print("[ERROR] Incorrect current password!")
            return
        
        new_pwd = input("Enter new password: ").strip()
        if not new_pwd:
            print("[ERROR] Password cannot be empty!")
            return
        
        confirm_pwd = input("Confirm new password: ").strip()
        if new_pwd != confirm_pwd:
            print("[ERROR] Passwords do not match!")
            return
        
        employee.password = _hash_pwd(new_pwd)
        self.save_employees()
        print("[SUCCESS] Password changed successfully!")

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
            name = input("Enter Name: ").strip().lower()
            res = [e for e in self.employees if name in e.name.lower()]
            if res: self._print_employee_table(res)
            else: print("Not found.")
        elif opt == 3:
            dept = input("Enter Dept: ").strip().lower()
            res = [e for e in self.employees if dept in e.department.lower()]
            if res: self._print_employee_table(res)
            else: print("Not found.")

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
        print("5. Change My Password")
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
        elif choice == 5:
            company.change_password(employee)
        elif choice == 0:
            company.logout_employee(employee)
            break
        else:
            print("Invalid choice! Choose between 0 to 5.")

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
        print("8. View & Approve/Reject Pending Leave Requests")
        print("9. View All Leave History Logs")  
        print("10. Generate Payslip for any Employee") 
        print("11. Unfreeze Employee Account")
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
            company.view_all_leave_history() 
        elif choice == 10:
            try:
                emp_id = int(input("Enter Employee ID to generate payslip for: "))
                emp = company._find_by_id(emp_id)
                if emp:
                    company.generate_payslip(emp)
                else:
                    print("Employee not found!")
            except ValueError:
                print("Invalid ID format.")
        elif choice == 11:
            company.unfreeze_employee()
        elif choice == 0:
            print("Goodbye!")
            print("Logging out Administrator (HR)...")
            break
        else:
            print("Invalid Choice! Choose between 0 to 11.")

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
        
        choice = input("Enter choice (1-2): ").strip()
        
        if choice == '1':
            attempts = 3
            success = False
            while attempts > 0:
                pwd = input("Enter Admin Password: ").strip()
                if _hash_pwd(pwd) == company.hr_password_hash:
                    print("\n[SUCCESS] Logged in as Administrator (HR)!")
                    success = True
                    admin_menu(company)
                    break
                else:
                    attempts -= 1
                    print(f"\n[ERROR] Incorrect Admin Password! Attempts remaining: {attempts}")
            if not success and attempts == 0:
                print("\n[ERROR] Too many failed login attempts. Access locked for this session.")
        elif choice == '2':
            try:
                eid = int(input("Enter Employee ID: "))
                emp = company._find_by_id(eid)
                if emp:
                    if emp.is_frozen:
                        print("\n[ERROR] Your account is FROZEN due to multiple failed login attempts! Please contact HR/Admin to unfreeze it.")
                        continue
                    
                    attempts = 3
                    success = False
                    while attempts > 0:
                        pwd = input("Enter Password: ").strip()
                        if emp.password == _hash_pwd(pwd):
                            print(f"\n[SUCCESS] Welcome back, {emp.name}!")
                            success = True
                            employee_menu(company, emp)
                            break
                        else:
                            attempts -= 1
                            print(f"\n[ERROR] Incorrect Password! Attempts remaining: {attempts}")
                    
                    if not success and attempts == 0:
                        emp.is_frozen = True
                        company.save_employees()
                        print("\n[ERROR] Too many failed login attempts! Your account has been FROZEN. Contact Admin.")
                else:
                    print("\n[ERROR] Invalid Employee ID!")
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