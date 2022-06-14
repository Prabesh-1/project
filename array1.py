# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 06:09:15 2022

@author: prabesh sharma
"""
"""
from array import array
weights=array('i',[62,73,44,94,14])
print(weights)
#print(help(array))
weights[0]=42
print(weights)
print(weights[3])
"""

from array import array
marks=array('i',[67,43,23,56])
total=marks[0]+marks[1]+marks[2]+marks[3]
avg=total/4
print(total)
print(avg)
marks[2]=73
total=marks[0]+marks[1]+marks[2]+marks[3]
avg=total/4
print(total)
print(avg)
print(max(marks))
print(sum(marks))
print(len(marks))
print(min(marks))

#calculate result of student(pass mark=40)?
#user defined type i.e. class
class student:
    pass
#use
s1=student()
s2=student()
print(type(s1))
print(type(s2))
#record sound and store on file(*.wav)
#play sound file.(*.wav)

