#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:44:53 2021
Modefied code: Dec. 21, 2021

Test1: Object Oriented Programming
@author: alibehfarnia
"""

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first[0] + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Ali', 'Behfarnia', 80000)
emp_2 = Employee('Test', 'Employee', 120000)

print(" ")
print("Full Name:")
print("----------")
print(Employee.fullname(emp_1))
print(" ")
print("Email:")
print("------")
print(emp_1.email.lower())