class Employee:
    def __init__(self, salary):
        self.salary = salary

    def role(self):
        return "Employee"


class Manager(Employee):
    def role(self):
        return "Manager"


e = Employee(3000)
m = Manager(5000)

print(e.role(), e.salary)
print(m.role(), m.salary)
