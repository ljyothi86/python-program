#program to check if a number is prime or not
num=29
#to take input from the user
num=int(input("enter a numbers:"))
#define a flag variable        
flag= False
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
         

