#python program to find the factorial of a number
#ex 5! 5x4x3x2x1   ex num<0
#ex 4! 4x3x2x1     ex num==0 for loop

#solution-1
"""
num =int(input("enter a number here:"))
fact=1
if num<0:

    print("factorial of 0 does not exist")

if num==0:
    print("factorial of 0is ",1)

if num>0:
    for i in range (1,num+1):
        fact=fact*i
    print("the factorial of the given number")
"""


#solution-2  Recursion ex  def add()
                                #3+4 ()


def factorial(a):
    if a==0:
        return 1
    else:
            return((a)*factorial(a-1))

num= int (input("enter a number here:"))
result = factorial(num)
print("the fcatorial of the given number is",result)
    
6
