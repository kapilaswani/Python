# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:30:32 2020

@author: Kapil Aswani
"""

##########################################
# Program to read three numbers and swap #
##########################################

a = int(input("Enter first Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

a,b,c = a,a+b,b+c

print(a,b,c)