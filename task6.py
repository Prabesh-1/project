# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 07:02:14 2022

@author: User
"""

#Enter start No:_1
#Enter stop No:_10
#print 1,2,3,....10
#sum=55
#average:5.5
#max:10
#min:1
start=None
stop=None
start=1
stop=10
i = 1
while(i<=10):
    print(i)
    i += 1
    
num = 10

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
   
n = int(input("Enter number"))
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)