# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:33:31 2020

@author: Kapil Aswani
"""

####################################################
# Program to find the simple and compound interest #
#   Simple Interest : A = P(1 + rt)                #
####################################################

p = float(input("Enter principle amount ($): "))
r = float(input("Enter Rate of Interest: "))
t = int(input("Number of Years: "))

si = float(p * (1 + (r * t/100)))
ci = float(p * (1 + r/100)**t)

print("Simple Interest: ",round(si,1))
print("Compound Interest: ",round(ci,1))