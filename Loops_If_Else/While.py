print("****WAP to illustrate while loop*******\n")

count =0
while (count < 4):
	count = count +1
	print(count)
	
#print() this print anyways does not do anything as this is blank


print("\n*********while program with break*******")
c =5
while (c < 4):
	#print(c)# this will print only the c value as 0
	c = c +1
	print(c)# this will print c value as 1 and breaks
	break
else:
	print("No Break")
	

l=[11,5,14,13,16,18]
print(l)
for i in l:
	if i%2==0:
		print( i, "divided by 2 =", i//2)
		l.remove(i)

print(l)