
# python program to print prime number an interval
# lower and upper case values((num 50/2)
lower=int(input("enter lower limit here:"))
upper=int(input("enter upper limit here:"))

for num in range(lower,upper+1):
    if num >1:
        for i in range (2,num):
            if num% i==0:
                break
            else:
                print(num)
