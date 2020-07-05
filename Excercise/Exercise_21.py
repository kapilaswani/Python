# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:36:03 2020

@author: Kapil Aswani
"""

#########################################
# Write a program to find the LEAP Year #
#########################################

yr = int(input("Enter Year (YYYY): "))

leap = yr % 4

if leap == 0:
    print (yr,"is a Leap Year")
else:
    print (yr,"not a leap Year")