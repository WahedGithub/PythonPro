amount = int(input('Enter the Amount:'))

if amount < 50:
	discount= amount*0.05
	print('discount:', discount)
	
else:
	discount = amount*0.10
	print('discount:', discount)
	
print("Net payable amount:", amount-discount)