#!/usr/bin/env python3

class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        #setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        #incrementing class variable
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #introduction of dunder methods
    def __repr__(self):
        #repr is used by devolopers
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        #str is used by end users
        return '{} - {}'.format(self.fullname(), self.email)
emp_1 = Employee('joe', 'smith', 50000)
emp_2 = Employee('jane', 'doe', 60000)

#to access the dunder methods you use repr() and str() but in generall you can acces by print(emp_1) or print(repr(emp_1))

print(emp_1)
