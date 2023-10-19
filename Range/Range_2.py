
print('\nQ1 This is divisible by 3 and 5')

list = []
for i in range(1, 51):
    if (i%3==0) and (i%5==0):
       list.append(i)
	   
print(list)

print('\nQ2 This is divisible by 3 and not by 5')
for i in range(1, 51):
    if (i%3==0) and (i%5!=0):
        list.append(i)
	
print(list)

print ('\nQ3the number divisible by 2 from the provided range')
num= int(input("Enter the num:"))
#in range(start, end+number will try till that step)
for i in range(3, num+0):
    if (i%5==0):
        print (i)

