# Employee Management System

A console-based **Employee Management System** built with Python using **Object-Oriented Programming (OOP)**. This project demonstrates clean class design, admin authentication, property-based data validation, JSON-based data persistence, CRUD operations, and payroll calculation.

---

## Features

* Admin Login / Authentication (username & password)
* Add a new employee
* View all employees in a formatted table (auto-sorted by Employee ID)
* Search employees by:
  * Employee ID
  * Name
  * Department
  * Position
* Update employee information (leave a field blank to keep its current value)
* Delete employees with confirmation
* Calculate Total Company Payroll
* Prevent duplicate Employee IDs
* Validate salary input (must be a positive number)
* Store employee records using JSON
* Automatically sort employees by Employee ID

---

## Technologies Used

* Python 3
* JSON

---

## Concepts Covered

* Object-Oriented Programming (OOP)
* Classes & Objects (`Admin`, `Employee`, `Employee_Manager`)
* Constructors (`__init__`)
* Properties (`@property` / setter) for salary validation
* Class Methods (`@classmethod`) — `from_dict()`
* Static Methods (`@staticmethod`) — `format_currency()`
* Object Serialization (`to_dict()` / `from_dict()`)
* Authentication
* JSON File Handling
* Exception Handling
* Input Validation
* Menu-Driven Applications

---

## Project Structure

```text
Employees-Managment-System/
│
├── Employes Management System.py
├── .gitignore
└── README.md
```

> **Note:** `employees.json` is created automatically when the program runs. It stores employee records locally and is excluded from the repository via `.gitignore` because it contains runtime data rather than source code.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/osaid400/Employees-Managment-System.git
```

2. Navigate to the project folder:

```bash
cd Employees-Managment-System
```

3. Run the program:

```bash
python "Employes Management System.py"
```

---

## Example Output

### Admin Login

```text
============ Welcome to Employee Management System =============
Enter Username: admin
Enter Password: 12345
Login to Employee Management System
```

### Main Menu

```text
=============== Employee Management Menu ===============
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Total Compnay Payroll
0. Exit
=========================================================
```

### View Employees

```text
========================================================================================================================
Employee Name        Employee ID          Department                Position                       Salary
========================================================================================================================
Ali                  101                  HR                        Manager                        Rs. 75,000
Ahmed                102                  IT                        Software Engineer             Rs. 90,000
Usman                103                  Finance                   Accountant                    Rs. 65,000
========================================================================================================================
```

### Search Employee

```text
--------------------------------------------------
Search By:
1. Search by ID
2. Search by Name
3. Search by Department
4. Search by Position
--------------------------------------------------
Enter your choice: 3
Enter the Department: IT

========================================================================================================================
Employee ID          Name                 Department                Position                       Salary
========================================================================================================================
Ahmed                102                  IT                        Software Engineer             Rs. 90,000
Hamza                106                  IT                        Network Administrator         Rs. 80,000
Umer                 114                  IT                        System Administrator          Rs. 85,000
========================================================================================================================
```

### Total Company Payroll

```text
=========================================================
Total Company Payroll: Rs. 985,000
=========================================================
```

### Delete Employee

```text
Enter the Employee ID: 121
Are you sure you want to delete Abdullah? (y/n): y
Employee Deleted Successfully!
```

---

## How Data Persistence Works

* On startup, the program checks whether `employees.json` exists.
* If the file exists, all employee records are loaded and converted into `Employee` objects.
* If it doesn't exist, a default set of sample employees is created and saved.
* Every time an employee is added, updated, or deleted, the full employee list is saved back to `employees.json`.
* This ensures employee data remains available even after closing and reopening the program.

---

## Future Improvements

* Search employees by Salary Range
* Sort employees by Salary
* Display highest and lowest-paid employee
* Export employee records to CSV
* Password hashing for admin login
* SQLite database integration
* Build a GUI version using Tkinter

---

## Learning Outcomes

This project helped me practice:

* Designing applications using Object-Oriented Programming
* Implementing encapsulation with properties and setters
* Building admin authentication flows
* Creating reusable classes and methods (`@classmethod`, `@staticmethod`)
* Managing persistent data using JSON
* Performing CRUD (Create, Read, Update, Delete) operations
* Validating user input and handling exceptions
* Building structured, menu-driven console applications

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400