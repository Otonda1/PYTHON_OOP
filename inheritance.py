#!/usr/bin/env python3

class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        #setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
#inheritance allows us to inherit attributes and methods from a parent class

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
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

dev_2 = Developer('john', 'doe', 70000, 'Python')
dev_3 = Developer('jane', 'doe', 80000, 'Java')

print(dev_2.email)
print(dev_2.prog_lang)
print(isinstance(dev_2, Developer))
print(issubclass(Developer, Employee))



