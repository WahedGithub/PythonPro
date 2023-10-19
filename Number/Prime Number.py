print('WAP to find all prime number in the given interval')

#Num = int(input('Enter the Number:'))# if int is not assign before input then it will consider it a a string and give a error saying str can't be taken as a int
for i in range (2,25):
	if i >1:
		for j in range(2, i):
			if (i%j==0): ##here we are dividing the input with i value.
				print(i, "is not a prime number as", i, "divided by", j, 'is', i//j)
				break
		else:
			print (i,"is a prime number")
	else:
		print(i, "is not a prime number")
			
print("\n******Prime number for a defined number********")
num = int(input("enter the number:"))

if num>1:
	for i in range(2, num):
		if num%i==0:
			print(num, "is not a prime number")
			print(i, "times", num//i, "is", num)
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number & negative")
	