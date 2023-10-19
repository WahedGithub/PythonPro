num = int(input("enter a number:"))
if (num >1):
	for i in range(2,num):
		if(num%i == 0):
			print(num, "number is not a prime" )
		#break
	#else:
	#	print (num, "number is a prime")
else:
	print(num,"number is a prime")