# python prograam  to check Armstrong number
#armstrong number: exple1:153=(1*1*1)+(5*5*5)+(3*3*3)
                     #      =  1+125+27
                       #    =153 that armstrong number
                # example2: 53 = (5*5)+(3*3)
                            #  =  25+ 9
                             # =   34 not armstrong number


num=int(input("enter a numberhere:"))
sum=0
temp=num
while temp>0:
     digit=temp%10
     cube=digit**3
     sum=sum+cube
     temp//=10

if sum==num:
     print("it is an armstrong number")
else:
     print("it is not an armstrong number")
                        
