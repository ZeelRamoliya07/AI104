"""
Create a class "Employee" with attributes name and salary. Implement overloaded operators +
and - to combine and compare employees based on their salaries.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(f"{self.name} & {other.name}", self.salary + other.salary)

    def __sub__(self, other):
        return abs(self.salary - other.salary)

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

def employee_menu():
    name1 = input("Enter first employee's name: ")
    salary1 = float(input("Enter first employee's salary: "))

    name2 = input("Enter second employee's name: ")
    salary2 = float(input("Enter second employee's salary: "))

    emp1 = Employee(name1, salary1)
    emp2 = Employee(name2, salary2)

    print("\nCombined Employee:", emp1 + emp2)
    print("Salary Difference:", emp1 - emp2)

employee_menu()
