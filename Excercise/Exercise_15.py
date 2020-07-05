# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:23:53 2020

@author: Kapil Aswani
"""

########################################
# Program to find the area of Triangle #
########################################

a = float(input("Enter Length of Side A: "))
b = float(input("Enter Length of Side B: "))
c = float(input("Enter Length of Side C: "))

s = (a+b+c)/2

area = float((s*(s-a)*(s-b)*(s-c)) ** .5)

print ("Area of Triange: ",round(area,2))