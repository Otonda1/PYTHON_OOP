#!/usr/bin/env python3

class Employee:
    def __init__(self, first, last, pay):
        #setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


#initialize instances
joe = Employee('joe', 'smith', 50000)
jane = Employee('jane', 'doe', 60000)

print(joe.email)
print(jane.email)
print(joe.fullname())