#python program to find the largest number among the three number
#chnage the values of num1,num2,num3
#for a differnt result
num1=10
num2=14
num3=12
#uncomment follwing line to take three number from use
#num1=float(input("enter first number:"))
#num2=float(input("enter second number:"))
#num3=float(input("enter three number:"))

if(num1>=num2)and(num1>=num3):
    largest=num1
elif(num2>=num1)and(num2>=num3):
    largest=num2
else:
    largest=num3
print("the largest number is ",largest)

    
