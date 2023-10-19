print('WAP to find the whole prime numbers not only the defined number')
Num = int(input('Enter the Number:'))
factor=0
for n in range(1,Num):
	#for x in range (2, n): #this line is of not use here need to understand
		if n%Num==0:##here we are dividing the n value with input
		    factor=factor+1
			#print (n, "is not a prime number")
			#break
		
	#else:
		#print (n,"is a prime number")
if factor==2:
	print(Num, "is a prime number")
else:
	print(Num, "is not a prime number")