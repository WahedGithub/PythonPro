#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
n=[]
for i in range (1500, 2700):
	if (i%7==0) & (i%5==0):
	 n.append(str(i))

print(','.join(n))

#Write a Python program that accepts a word from the user and reverse it
#w = raw_input("Enter the word:")
#print (w[::-1])

#Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers= [1,2,3,4,5,6,7,8,9]
count_odd=0
count_even=0
for n in numbers:
	if n%2 :
		count_even+=1
	else:
		count_odd+=1
			
print("Number of Even:", count_even)
print("odd:", count_odd)


print("\n********WAP for FOR loop********")
l= ["Abdul", 123, "wahed"]
for i in l: #for printing in seprate lines this can be used
	print("for printing in seprate lines this can be used:", i)
	

print("\n******WAP for For loop using Dictionary*******")
d=dict()
d['xyz']=123
d[23]=345
for i in d:
	print("%s %d" %(i, d[i]))
	
	
