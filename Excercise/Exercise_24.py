# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:32:56 2020

@author: Kapil Aswani
"""

####################################################
# Program to input 3 numbers are print the largest #
####################################################

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

high = x

if y >= high:
    high = y
if z >= high:
    high = z

print("Highest Number:",high)
    
