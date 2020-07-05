# -*- coding: utf-8 -*-
"""
Created on Sat May 30 07:18:29 2020

@author: Kapil Aswani
"""

##################################################################
# Program to input three number and perform following operations #
#                                                                #
# Sum1 = Sum for all input numbers                               #
#                                                                #
# Sum2 = Sum of all non-duplicates numbers                       #
##################################################################

x = int(input("Enter first Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

sum1 = x+y+z

sum2 = 0

if x != y and x != z :
    sum2 += x
if y != x and y != x :
    sum2 += y
if z != x and z != y :
    sum2 += z
    
print("Numbers are:", x, y, z, sep=" ")
print("SUM of three numbers:",sum1)
print("SUM of non-duplicate numbers:",sum2)