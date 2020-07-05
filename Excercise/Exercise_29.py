# -*- coding: utf-8 -*-
"""
Created on Sat May 30 07:45:31 2020

@author: Kapil Aswani
"""

########################################################
# Program to get choice to calculate Area or Perimeter #
########################################################

print("!!! W-E-L-C-O-M-E !!!")
print("Choose 1: Calculate the Area: ")
print("Choose 2: Calculate the Perimeter: ")
choice = int(input("Enter the choice: "))

if choice == 1 :
    x = float(input("Enter side A: "))
    y = float(input("Enter side B: "))
    area = x*y
    print("Area Equals: ",area)
elif choice == 2 :
    x = float(input("Enter side A: "))
    y = float(input("Enter side B: "))
    perimeter = float(2*(x + y))
    print("Perimeter Equals: ",perimeter)
else :
    print("Wrong Choice")