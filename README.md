# Employee Management System

A beginner-friendly console-based Employee Management System built with Python. This project demonstrates the use of functions, JSON file handling, input validation, searching, updating records, and menu-driven programming to manage employee information.

---

## Features

* Add a new employee
* View all employees in a formatted table
* Search employees by Employee ID
* Search employees by Name
* Update employee information
* Delete employees with confirmation
* Prevent duplicate Employee IDs
* Validate user input
* Store employee records using JSON
* Automatically sort employees by Employee ID

---

## Technologies Used

* Python 3
* JSON

---

## Concepts Covered

* Functions
* Lists
* Dictionaries
* JSON File Handling
* File Read/Write
* Loops
* Conditional Statements
* Input Validation
* Exception Handling (`try` / `except`)
* Searching Algorithms
* Updating Records
* Menu-Driven Applications

---

## Project Structure

```text
Employee-Management-System/
│
├── employee_management_system.py
├── .gitignore
└── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/osaid400/Employee-Management-System.git
```

2. Navigate to the project folder:

```bash
cd Employee-Management-System
```

3. Run the program:

```bash
python employee_management_system.py
```

---

## Example Output

### Main Menu

```text
=============== Employee Management Menu ===============
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
0. Exit
```

---

### View Employees

```text
==============================================================================================================
Employee ID         Name                 Department         Position                  Salary
==============================================================================================================
101                 Ali                  HR                 Manager                   Rs. 75,000
102                 Ahmed                IT                 Software Engineer         Rs. 90,000
103                 Usman                Finance            Accountant                Rs. 65,000
==============================================================================================================
```

---

### Search Employee

```text
Search By:
1. Search by ID
2. Search by Name

Enter your choice: 2
Enter the Employee Name: ali

==============================================================================================================
Employee ID         Name                 Department         Position                  Salary
==============================================================================================================
101                 Ali                  HR                 Manager                   Rs. 75,000
==============================================================================================================
```

---

### Add Employee

```text
Enter the Employee ID: 121
Enter the Employee name: Abdullah
Enter the Department name: Finance
Enter the Position name: Analyst
Enter the Salary: 85000

New Employee Added Successfully!
```

---

### Update Employee

```text
Enter the Employee ID: 121

Current Details:
Employee ID: 121
Name: Abdullah
Department: Finance
Position: Analyst
Salary: Rs. 85,000

Enter the new Position name: Senior Analyst

Employee Updated Successfully!
```

---

### Delete Employee

```text
Enter the Employee ID: 121

Are you sure you want to delete Employee Abdullah? (y/n): y

Employee Deleted Successfully!
```

---

## Future Improvements

* Search employees by Department
* Search employees by Position
* Sort employees by Salary
* Calculate total company payroll
* Display highest and lowest salary
* Export employee records to CSV
* Add login/authentication system
* Convert the project to Object-Oriented Programming (OOP)
* Integrate with SQLite database

---

## Learning Outcomes

This project helped me practice:

* Building menu-driven console applications
* Managing structured data using JSON
* Creating reusable functions
* Performing CRUD (Create, Read, Update, Delete) operations
* Validating user input
* Searching and updating records
* Displaying data in formatted tables
* Organizing code for readability and maintainability

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
