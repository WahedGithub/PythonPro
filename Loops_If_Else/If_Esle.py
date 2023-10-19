amount = int(input("Enter amount:"))

if amount< 1000:
	discount=amount*0.05
	print('Discount:', discount)
else:
	discount=amount*0.10
	print('Discount:', discount)

print("Net payable:", amount-discount)



print("\n***WAP to check if basic functionality***")
i=16
if i>15:
	print(i, "is greater than 15")
else:
	print("I am not in if")

	
print("\n **** WAP****")	
list=[1,4,7,3,6]
i=1
while (i < len(list)):
	if list[i] %2==0:
	 print(list[i], end=" ")
	i +=1

