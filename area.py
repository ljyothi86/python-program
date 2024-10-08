# pthon program to find area of circule

"""
a=5
b=6
c=7
a=float(input("enter the first side:"))
b=float(input("enter the second side:"))
c=float(input("enter the thred side:"))
s=(a+b+c)/2
#calculate the area
area=(s*(s-a)*(s-b)*(s-c))** 0.5
print("the area of the traingle %0.2f"%area)

"""
#square root programs
"""
import math
num=int(input("enter a number"))
sqroot=math.sqrt(num)
print("the square root of {num}is",sqroot)
"""
#program to check if a number is prime or not
num=29
#to take input from the user
num=int(input("enter a numbers:"))
#define a flag variable        
flag = false
if num ==1:
    print(num,"isnot a prime number")
elif num>=1:
    for i in rangege(2,num):
        if(num%i)==0:
            flag=true
        break
if flag:
     print(num,"is not a prime number")
else:
    print(num,"is a prime number")
         
