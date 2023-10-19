bin1 = input("Enter binary number: ")
bin2 = bin1
power = 0
deci = 0
while bin1>0:
		rem = bin1 % 10
		deci += rem * 2 ** power
		power +=1
		bin1 /=10
	
print "The decimal number of given binary number %d is %d" %(bin2,deci)