#python program to check prime number
#ex 3,5,7,11,13,17.......not divisable
num=int(input("enter a number here:"))
if num ==1:
        print("it is not aprime number")
if num >1:
    for i in range(2,num):
        if num % i==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")

