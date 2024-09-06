'''Define a Employee class with attributes role, department &
salary. This class also showDetails() method'''

'''Create an Engineer class that inherits properties from Employee
& has additional attributes: name & age 
'''


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept 
        self.salary = salary

    def showDetails(self):
        print("role =",  self.role)
        print("dept  =", self.dept)
        print("salary =", self.salary)
        print("name = ", self.name)
        print("age =", self.age)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        super().__init__("Engineer", "IT", "Rs 50000")


e1 = Engineer("Goutam", 20)
e1.showDetails()