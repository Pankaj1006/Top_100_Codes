num=int(input(“Enter a number”))
sum=0
temp=num
while temp>0:
f=1
i=1
rem=temp%10
while i<=rem:
f=f*1
i=i+1
Sum=sum+f
temp=temp//10
Print("sum is {}".format(sum))
