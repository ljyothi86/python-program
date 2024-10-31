#python program  largest Among three numbers
num1=int(input("enter 1stlargest number:"))

num2=int(input("enter 2nd largest number:"))
num3=int(input("enter 3th largest number:"))

if(num1>num2)and(num1>num3):
    print(num1,"is a largest number")
elif(num2>num1)and(num2>num3):
    print(num2,"is a largest number")
else:
    print(num3,"is a largest number")
    
