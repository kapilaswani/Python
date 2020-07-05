# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:12:40 2020

@author: Kapil Aswani
"""

##################################################################
# Convert height provided by user in Centimeter to inch and foot #
##################################################################

height = float(input("Enter Height in Centimeter (CM):"))
inch = height/2.54
feet = inch/12

print(height,round(inch,2),round(feet,2))