# Employees Management System

A console-based Employees Management System built with Python using Object-Oriented Programming (OOP) principles. It models real HR operations — employee records, leave applications with admin approval, payslip generation, and payroll analytics — with secure password hashing, login lockout protection, and a modular package structure.

---

## Features

* **Admin / HR Panel:**
  * Secure Admin Login (hashed password, 3-attempt session lock)
  * Add New Employee
  * View All Employees Roster
  * Search Employee (by ID, Name, or Department)
  * Update Employee Details
  * Delete Employee
  * Department-Wise Payroll Analytics Dashboard
  * Sort & Filter Employees List (by Salary, Name, or Department)
  * View & Approve/Reject Pending Leave Requests
  * View All Leave History Logs
  * Generate Payslip for Any Employee
  * Unfreeze Employee Account (after failed-login lockout)

* **Employee Panel:**
  * Secure Login (hashed password, 3-attempt account lockout)
  * View My Profile & Department Details
  * Apply for Leave (Full Day / Half Day, future dates only)
  * View My Leave History & Status
  * Generate & Download My Payslip (`.txt`)
  * Change My Password

* **Data & Security Features:**
  * SHA-256 Password Hashing (no plaintext passwords stored)
  * 3-Attempt Login Lockout — employee accounts auto-freeze after 3 failed attempts and require admin unfreezing; admin login locks for the session after 3 failed attempts
  * Persistent JSON Storage for employees and leave requests
  * Auto-generated Payslips with Allowance, Medical, Income Tax, and Leave-based Deductions, archived monthly by name (`payslip_<ID>_<Month>_<Year>.txt`)
  * Input validation and exception handling throughout

---

## Technologies Used

* **Python 3** (Object-Oriented Programming)
* **JSON Module** (Data persistence)
* **hashlib** (SHA-256 password hashing)
* **Datetime Module** (Payslip archiving, leave date validation)
* **OS Module** (Directory and file handling)

---

## Project Structure

```text
Employees-Management-System/
│
├── data/
│   ├── employees.json          # Persistent employee records (gitignored)
│   └── leave_requests.json     # Persistent leave request records (gitignored)
│
├── Salary_Slips/               # Auto-generated monthly payslips (gitignored)
│
├── src/                        # Source code package
│   ├── __init__.py
│   ├── models.py                 # Employee class and password hashing helper
│   ├── manager.py                 # EmployeeManager class — persistence, payroll, leave logic
│   └── UI.py                      # Admin and Employee menus, display formatting
│
├── .gitignore                  # Excludes __pycache__, Salary_Slips, and local data
├── main.py                     # Application entry point
└── README.md
```

> **Note:** `data/employees.json` and `data/leave_requests.json` are created automatically on first run. They store employee records and leave history locally and are excluded from the repository via `.gitignore`.

---

## How to Run

Clone the repository

```bash
git clone https://github.com/osaid400/Employees-Management-System.git
```

Move into the project folder

```bash
cd Employees-Management-System
```

Run the program

```bash
python main.py
```

---

## Example Outputs

### Main Menu

```text
================== WELCOME TO EMPLOYEES MANAGEMENT SYSTEM =======================

============================ SYSTEM MENU ======================================
1. Login as HR/Admin
2. Login as Employee
0. Exit
=================================================================================
```

### Employee Login Lockout in Action

```text
Enter Employee ID: 105
Enter Password: wrong1
[ERROR] Incorrect Password! Attempts remaining: 2

Enter Password: wrong2
[ERROR] Incorrect Password! Attempts remaining: 1

Enter Password: wrong3
[ERROR] Incorrect Password! Attempts remaining: 0

[ERROR] Too many failed login attempts! Your account has been FROZEN. Contact Admin.
```

### Employee Panel

```text
==================== EMPLOYEE PANEL (Bilal) ====================
1. View My Profile & Department Details
2. Apply for Leave (Full Day / Half Day)
3. View My Leave History & Status
4. Generate & Download My Payslip (.txt)
5. Change My Password
0. Logout
==============================================================================
```

### Apply for Leave

```text
========================== Leave Application ==========================
1. Full Day Leave
2. Half Day Leave
=======================================================================
Select type (1 or 2): 1
Enter Leave Date (DD-MM-YYYY): 14-08-2026
Enter Reason for Leave: Want to go hospital with my Brother!

Applying for Full Day Leave on 14-08-2026...

[SUCCESS] Leave application submitted successfully!
```

### Admin Panel — Payroll Analytics

```text
======================================================================
Department           Total Employees          Total Payroll
======================================================================
HR                          3                Rs. 160,000
IT                          3                Rs. 255,000
Finance                     3                Rs. 172,000
======================================================================
Total Company Payroll across all departments: Rs. 587,000
======================================================================
```

### Payslip (.txt output)

```text
=====================================================
                 OFFICIAL COMPANY PAYSLIP
                 Month: August 2026
=====================================================
Employee Name : Bilal
Employee ID   : 105
Department    : Sales
Position      : Sales Executive
-----------------------------------------------------
Basic Salary  : Rs. 70,000
Allowance (5%): Rs. 3,500
Medical (5%)  : Rs. 3,500
Gross Salary  : Rs. 77,000
-------------------------------------------------------
Income Tax (5%): Rs. 3,500
Approved Leaves: 1.0 day(s)
Leave Deduction: Rs. 2,333
Total Deductions: Rs. 5,833
-------------------------------------------------------
Net Pay       : Rs. 71,167
=======================================================
```

---

## Concepts Covered

* **Object-Oriented Programming (OOP):** Class design and encapsulation (`Employee`, `EmployeeManager`), with a validated `salary` property (`@property` / `@salary.setter`).
* **CRUD Operations:** Full employee lifecycle — add, search, update, delete.
* **JSON Data Serialization:** Persistent storage via `to_dict()` / `from_dict()` for both employee records and leave requests.
* **Security:** SHA-256 password hashing and a 3-attempt lockout system to slow down password guessing, for both employee and admin logins.
* **Business Logic & Validation:** Payslip calculations combining allowances, medical, tax, and leave-based deductions; leave applications restricted to future dates.
* **Admin/Employee Role Separation:** Distinct menus and permissions — employees manage their own leave and payslips; admins manage the whole roster and approvals.
* **Modules & Packages:** Code organized into a `src/` package (`models.py`, `manager.py`, `UI.py`), separating data, business logic, and presentation, with `main.py` as the entry point outside the package.
* **Defensive Programming:** Input validation and exception handling (`try`/`except`/`raise`) across all menus and operations.
* **Date & Time Handling:** Leave date validation and monthly payslip archiving via `datetime`.

---

## How the Leave & Payslip System Works

* Employees **apply** for leave with a type, future date, and reason — this creates a *pending* request.
* Admins review pending requests and **approve or reject** them from the Admin Panel.
* When a payslip is generated, only **approved** leaves count toward the deduction — Full Day leaves deduct one day's pay, Half Day leaves deduct half.
* Payslips are archived monthly per employee, so regenerating a payslip in the same month overwrites that month's file rather than creating duplicates.

## How the Login Lockout Works

* Both Employee and Admin logins allow 3 attempts per session.
* On an employee's 3rd consecutive failure, their account is marked `is_frozen` and they can no longer attempt login until an admin unfreezes it from the Admin Panel.
* On the Admin's 3rd consecutive failure, access is locked for that session only (the admin can simply restart the app to try again — this is a lighter protection than the employee lockout since there is only one admin account).

---

## Future Improvements

* Salted password hashing (current hashing is unsalted)
* Move admin credentials out of source code (environment variables or a config file)
* Unique request IDs for leave requests, instead of matching by employee ID + date + reason
* Leave balance/quota system per employee
* SQLite or PostgreSQL integration replacing JSON persistence
* Graphical User Interface (Tkinter)

---

## Learning Outcomes

This project helped me practice and solidify key software engineering concepts:

* **Encapsulation in practice:** Keeping salary validation inside the `Employee` class via a property setter.
* **Security fundamentals:** Applying password hashing and brute-force lockout protection consistently across two different login flows (admin and employee).
* **Payroll logic:** Translating real-world payroll rules (allowances, tax, leave-based deductions) into a working calculation.
* **Approval workflows:** Separating leave "application" from "approval," similar to the loan/checkbook workflow built for the Bank Management System.
* **Modular project structure:** Splitting a single-file project into a `models` / `manager` / `UI` / `main` package, and deciding which lines of input-heavy methods belong in the manager versus the UI layer.

---

## Author

**Muhammad Abdullah Farooq**

GitHub: [https://github.com/osaid400](https://github.com/osaid400)