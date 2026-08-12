# =======================================
# Employees Management System
# Author: Muhammad Abdullah Farooq
# Language: Python 3.11
# =======================================

import sys
from src.manager import EmployeeManager
from src.models import _hash_pwd
from src.UI import admin_menu, employee_menu

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