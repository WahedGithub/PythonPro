a, b = 0,4
while b < 200:
	a, b= b,a+b # here it will add the previous number with 
	print (b)
	
# prints the b value =4 and now a, b= b, a+b here a is assigned to b and b= a+b 0+4=4, then 4+4, 4+8, 8+12
print()
a,b =1,2
while b < 30:
	a,b=b, a+b
	print(b)

x= 'awsesome'
def myf():
	global x
	x= 'fantastic'
	print("python is", x)
	
myf()

print("python is ", x)