num1= int(input("Enter the Num1:"))
num2= int(input("Enter the Num2:"))
num3= int(input("Enter the Num3:"))

#and or symbol(&) both can be used
if num1>num2 and num2>num3:
	print (num1,  'is bigger')

elif num2>num1 & num1>num3:
	print (num2, ' is bigger')

elif num1==num2 & num2==num3:
	print ("All are equal")
	
else:
 print (num3, "is bigger")