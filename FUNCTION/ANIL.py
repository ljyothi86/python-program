#create and call a function
"""
def my_function():
    print("hello from a function")
my_function()
"""
# function parameters
"""
def my_function(fname):
    print(fname + "refsnes")
my_function("Emil")
my_function("goole")
my_function("chinalss")
"""
#default parameter value
"""
def my_function(country ="norway"):
    print(" i am from "+ country)
my_function("sweden")
my_function("india")
my_function("india")
my_function()
my_function("Brazil")
"""
#let a function return a value?
"""
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
"""
# Recursion
"""
def tri_recursion(k):
    if(k>0):
        result= k+tri_recursion(k-1)
        print(result)
    else:
          result=0
    return result
print("\n\nRecursion Example result")
tri_recursion(6)
"""
# Alambda function that adds 10 to the number passed in as an argument?

"""
x=lambda a: a+ 10
print(x(5))
"""
#A lambda function that multiplies argument a with argument b
"""
x=lambda a,b: a*b
print(x(5,6))
"""
#a lambda function that sums argument a,b, and c
x= lambda a,b,c: a+b+c
print(x(5,6,2))



