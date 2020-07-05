# -*- coding: utf-8 -*-
"""
Created on Sat May 30 07:05:39 2020

@author: Kapil Aswani
"""

#########################################
# Input 3 numbers are find the smallest #
#########################################

x = y = z = 0

x = int(input("Enter number X: "))
y = int(input("Enter number Y: "))
z = int(input("Enter number Z: "))

small = x

if y < small :
    small = y
if z < small :
    small = z

print("Smallest number is ",small)
    