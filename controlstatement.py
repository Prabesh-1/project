# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 06:42:05 2022

@author: prabesh sharma
"""

#control statement
#if statement 
#select case statement

#if statements
#data types
    #bool,int complex,string,array,dict,class,set,tuple,list,float

#operators
    #assignment 
    #arithmetic
    #relational
    #logical
    #others
    
# condition
#(value1 relationaloperator value2)->True/False
#print(10>3)
"""
if condition:
    statement(s)
    #declare,input,process,output
"""
#Example
"""
num1=90
num2=9
if(num1>num2):
    print("Hello")
    print("Hii")
    print("How are you?")
print("Welcome to broadway")
"""
#Example-2
"""
num1=input("Enter any number:")
num1=int(num1)#type conversion(str->int)
if(num1==0):
    print("zero")
if(num1!=0):
    print("Non-zero")
"""
#Example-3
#writea program which print the number value.
#(i.e. 1-> one)
num1=input("Enter any number(0-9):")
num1=int(num1)
if num1==0:
    print("Zero")
if num1==1:
    print("one")
if num1==2:
    print("two")
if num1==3:
    print("three")
if num1==4:
    print("four")
if num1==5:
    print("five")
if num1==6:
    print("six")
if num1==7:
    print("seven")
if num1==8:
    print("eight")
if num1==9:
    print("nine")
if num1>9:
    print("other")
if num1<0:
    print("other")