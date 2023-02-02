num=int(input(“enter the number”))
for i in range(2, num+1):
	if num<0:
		print("sorry no factor")
	elif num%i==0:
		print("the factor of",num,"is",i)
