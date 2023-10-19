#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

#Hints: 
#Consider use range(#begin, #end) method

l=[] #basic funda whenever u have to take range and do some operation create an empty list and assign
for i in range(200, 301):
    if (i%7==0) and (i%5!=0):
        l.append(str(i)) #str is used for joining by separating with comma

print (l)
#print (','.join(l))# ','separates the values by joining in sequence


print('''\n Question.X=200 Z=2000 Print the numbers divisible by 7 and should not be the multiple of 5 from 
the Range given above?''')
for i in range(20,77):
	if(i%7==0) and (i%5!=0):
		print (i)

