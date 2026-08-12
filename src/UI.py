# src/UI.py

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