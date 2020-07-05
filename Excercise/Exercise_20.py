# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:26:36 2020

@author: Kapil Aswani
"""

################################
# Program to calculate express #
################################
import math

x = float(input("Enter the Number - x: "))
y = float(input("Enter the Number - y: "))
z = float(input("Enter the Number - z: "))

ca = float(4*math.pow(x,4) + 3*math.pow(y,3) + 9*z + 6*math.pi)

# Display Results

print(round(ca,2))