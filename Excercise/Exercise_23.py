# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:11:17 2020

@author: Kapil Aswani
"""

#####################################################
# Program to taka a number and check if Even or Odd #
#####################################################

num = int(input("Please Enter Number: "))

result = num%2

if result == 0:
    print ("Even Number: ",num)
else: 
    print ("Odd Nunber: ",num)