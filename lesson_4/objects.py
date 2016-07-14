__author__ = 'sekely'

'''
One of the biggest programming approaches today is the OOP - Object Oriented Programming.

when we are talking about object, we are referring to 2 things - the class and the instance.
objects can give attributes to instances, and can inherit attributes from other objects.

think of that:
a class is "child"
"Joe" is an instance of "child".

every "child" genetically inherit properties from "father" and "mother"

there is one general class that all class inherit from - "object"
'''


# Example
class Person(object):
    first_name = None
    last_name = None

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Employee(Person):
    salary = None

    def __init__(self, first_name, last_name, salary):
        super(Employee, self).__init__(first_name, last_name)
        self.salary = salary

    def raise_salary(self, new_salary):
        self.salary = new_salary


class Boss(Employee):
    employee_list = []

    # no __init__!
    # the class will use the Employee __init__ as default

    def add_employee(self, emp):
        self.employee_list.append(emp)

# creating an instance is like calling a method, but you should pass the params the are in __init__
# calling or using a property is done (generally) using "."

john = Employee('John', 'Smith', 700)  # instance of Employee
bob = Employee('Bob', 'Lee', 800)      # instance of Employee
alice = Boss('Alice', 'Chains', 1000)  # instance of Boss

alice.add_employee(john)
alice.add_employee(bob)
alice.raise_salary(1100)

print(bob.salary)                     # 800
print(alice.employee_list)            # what will be printed?
print(alice.employee_list[0].salary)  # 700

'''
you can do a lot with classes and instances.
in this course scope, we will touch only the tip of the iceberg when it comes to objects
'''

isinstance(alice, Boss)      # True
isinstance(alice, Employee)  # True
isinstance(bob, Boss)        # False
