#in range(start, end+number will try till that step)

num = int(input("Enter the num:"))
for num in range(2, num+1):
	for i in range(2, num):
		if num%i ==0:
			print(num, "num is not a prime number it is divisible by", i)
			break
		else:
			print(num, "num is a prime number")




