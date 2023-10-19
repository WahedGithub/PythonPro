num1 = num2= input("Enter the Decimal Number: ")
bin1 = ''
while num1>0:
	rem = num1 %2
	bin1 +=str(rem)
	num1 /=2
print "The number %d is %s" %(num2, bin1[::-1])