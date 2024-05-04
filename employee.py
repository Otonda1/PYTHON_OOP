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

    #introduction of a class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #introduction of a class method as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    #introduction of a static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

#changing the raise amount using the class method
Employee.set_raise_amt(1.05)
#using the class method as an alternative constructor
emp_str_1 = 'john-doe-70000'
Employee.from_string(emp_str_1)



print('NUMBER OF EMPLOYEES IS {}'.format(Employee.num_of_emps))
#initialize instances
joe = Employee('joe', 'smith', 50000)
jane = Employee('jane', 'doe', 60000)

import datetime
print(joe.is_workday(datetime.date(2021, 9, 25)))

