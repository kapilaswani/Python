# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:41:19 2020

@author: Kapil Aswani
"""

################################################
# Program to input numbers and check condition #
################################################

x = int(input("Enter Number x: "))
y = int(input("Enter Number y: "))

z = int (x%y)

if z == 0:
    print("Number",z,"first number fully divided by second number")