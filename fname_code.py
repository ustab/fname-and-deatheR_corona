# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:33:07 2022

@author: Anesthesia
"""
'''
Write a program that 

Takes the first name from the user and compares it to yours,
Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."
'''
fn=input("enter fname:")
yfn=input("yours fname:")
if fn==yfn:
    print("Hello, Joseph! The password is : W@12")
else:
   print("Hello, Amina! See you later.")