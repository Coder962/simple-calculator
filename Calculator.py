# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 20:16:11 2022

@author: Niranjan
"""

import math 


name = input("Enter your name:   ")
print("Hello ",name , "welcome to the calculator")

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

num3 = num1*num2
print("Product is:  ", num3)

num4 = num1/num2
print("Division is:  ", num4)

num5 = num1-num2
print("Subtraction is:  ", num5)

num6 = num1+num2
print("Addition is:  ", num6)

# menus

print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Square Root")

ch=int(input("Enter Choice(1-6): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c = a+b
    print("Sum = ", c)  
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c = a-b
    print("Difference = ", c)  
elif ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c = a*b
    print("Product = ", c)  
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c = a/b
    print("Quotient = ", c)  
elif ch==5:
    a=int(input("Enter Number :"))
    b = a*a
    print("Square = ", b)  
elif ch==6:
    a=int(input("Enter Number:"))
    b = math.sqrt(a)
    print("Square root = ", b) 
else:
    print("Invalid Choice")
           
