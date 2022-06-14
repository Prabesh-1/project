# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 18:52:32 2022

@author: prabesh
"""
#task-6
#Enter id:_1
#Enter name:_Raj
#Enter sub1:_56
#Enter sub2:_54
#Enter sub3:_45
#Total:155
#average:...
#result:PASS
#create functions to solve the resut processing system.

def personal_details():
    name, Id = "prabesh", 1
    print("Name: {}\nId: {}".format(name,Id))

personal_details()
def calc_total(sub1,sub2,sub3):
    print(sub1+sub2+sub3)
    print((sub1+sub2+sub3)/3)
sub1=int(input("Enter a sub1 marks:"))
sub2=int(input("Enter a sub2 marks:"))
sub3=int(input("Enter a sub3 marks:"))
calc_total(sub1,sub2,sub3)

if sub1>=40 and sub2>=40 and sub3>=40:
    print("result:PASS")
else:
    if sub1<=40 and sub2<=40 and sub3<=40:
        print("result:fail")

