# -*- coding: utf-8 -*-
"""
Created on Sat May 30 07:31:14 2020

@author: Kapil Aswani
"""

####################################################################
# Program to test the divisibility of a number with another number #
####################################################################

x = int(input("Enter first number: "))
y = int(input("Enter Second number: "))

result = x%y

if result == 0 :
    print(x," is divisible by ",y)
else :
    print(x," is NOT divisible by ",y)
