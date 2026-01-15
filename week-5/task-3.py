class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Name:", self.name)


class Student(Person):
    def info(self):
        print("Student name:", self.name)


p = Person("John")
s = Student("Alice")

p.info()
s.info()
