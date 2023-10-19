print("**********WAP to print numbers using break**********\n")

nums= [1,2,3,4,5]
for num in nums:
	if num == 3:
		print('Found!')
		break
	print(num)

print("**********WAP to print numbers using continue**********\n")
nums= [1,2,3,4,5]
for num in nums:
	if num == 3:
		print('Found!')
		continue
	print(num)
	
print("\n**********WAP to print letter and number**********")
nums= [1,2,3,4,5]
for num in nums:
	for letter in 'abc':
		print(num, letter)
		
