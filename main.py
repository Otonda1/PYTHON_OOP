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

print('NUMBER OF EMPLOYEES IS {}'.format(Employee.num_of_emps))
#initialize instances
joe = Employee('joe', 'smith', 50000)
jane = Employee('jane', 'doe', 60000)


print(joe.email)
print(jane.email)

#running methods using instances
print(joe.fullname())

#running methods using class
print(Employee.fullname(jane))
print(joe.pay)
joe.apply_raise()
print(joe.pay)
#print(joe.__dict__)
print('NUMBER OF EMPLOYEES IS {}'.format(Employee.num_of_emps))