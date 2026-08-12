# src/models.py

import hashlib

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