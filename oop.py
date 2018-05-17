# Python Object-Oriented Programming

import datetime

class IncompleteClass:
    pass
    # include this when you have an empty class that
    # you'll get back to


class Employee:

    # hard-code classwide info here
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # self.varname doesn't have to be the same as the
        # argument but it should be for ease of readability
        self.first = first
        self.last = last
        self.pay = pay

        # every time the class is instantiated
        # increment the number of employees
        Employee.num_of_emps += 1

    # @property decorator is for when a method is
    # defined like a method but accessible like an attribute
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # method that changes values of other things set by other methods
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # runs whenever you del an attribute
    @fullname.deleter
    def fullname(self, name):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # for methods that change the attributes of the
    # entire class instead of an instance
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # for methods that substantiate an instance of
    # a class using a particular input
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # doesn't access instance or class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __repr__(self):
        # this is another special method
        # it produces a log for dev debugging
        # if __str__ doesn't exist, uses __repr__ as backup
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        # produces something readable by the user
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        # decides what the + sign does
        return self.pay + other.pay


emp_1 = Employee('John', 'Smith', 50000)
emp_1.fullname = 'Corey Schafer'
emp_1.first

emp_2 = Employee('Test', 'User', 60000)
emp_1 + emp_2

del emp_1.fullname

repr(emp_1)
str(emp_1)
print(emp_1)


# arguments are class this class inherets from
class Developer(Employee):

    # overrides Employee class raise amount
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        # super() passes arguments to parent class's method
        super().__init__(first, last, pay)
        # 👇 another option that does the exact same
        # as above. super() is better (used more).
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


# returns a bunch of important info about inheritance of this subclass
help(Developer)


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        # passes arguments to parent class's method
        super().__init__(first, last, pay)
        if employees is None:
            # don't set default arguments as mutable
            # objects like dictionaries or lists
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# function that tests whether object is instance of a Class
isinstance(mgr_1, Manager)
isinstance(mgr_1, Developer)
isinstance(mgr_1, Employee)

issubclass(Developer, Employee)
issubclass(Manager, Developer)


print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 70000, 'Java')
print(dev_1.prog_lang)
print(dev_2.prog_lang)

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
Employee.set_raise_amount(1.05)

# this is borning and manual but it works to set values.
# it's easier to just define an __init__ once inside the class tho
emp_1.first = 'Corey'
emp_2.last = 'Schafer'

# this is better:
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# 2 ways to call a method:
#   1. call it as a method with .notation() on the object
emp_1.fullname()
#   2. call it as a function with ClassName.notation(object)
Employee.fullname(emp_1)

print(emp_1.pay)  # 50,000
emp_1.apply_raise()
print(emp_1.pay)  # 52,000

print(Employee.raise_amount)  # 1.04
print(emp_1.raise_amount)  # 1.04
print(emp_2.raise_amount)  # 1.04

# change class variable for all instances of the class
Employee.raise_amount = 1.05
print(Employee.raise_amount)  # 1.05
print(emp_1.raise_amount)  # 1.05
print(emp_2.raise_amount)  # 1.05

# change class variable for only 1 instance of the class
emp_1.raise_amount = 1.1
print(emp_1.raise_amount)  # 1.1

# get all info contained in class instance:
print(emp_1.__dict__)
# {'first': 'Corey',
# 'last': 'Schafer',
# 'pay': 52000,
# 'email': 'Corey.Schafer@company.com'}

print(Employee.num_of_emps)  # 2
