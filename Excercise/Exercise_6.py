# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 06:55:54 2020

@author: Kapil Aswani
"""

############################################################
#Program to calculate the BMI (Body Mass Index) of a person#
############################################################

weight = float(input("Enter your weight in KG(kilograms): "))
height = float(input("Enter your height in Meters: "))

#Formula used for calculation

result = weight / (height*height)


#Display Results

print("\nBody Mass Index(BMI):",result)