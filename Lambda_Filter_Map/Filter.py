##filter(logic/expression, input)
l1= [10,3,5,2,20]
print('''\n Method-1
***********WAP to find even numbers from a list by applying a filter with function**********''')
def m1(x):
	if x%2 ==0:
		return True
	else:
		return False
print(list(filter(m1,l1)))

l2= [1,2,3,4,5,6,7,8,9,10]
print('''\n\n Method-2
***********WAP to apply a filter without function**********''')
print(list(filter(lambda x:x%2==0, l2)))
print(tuple(filter(lambda x:x%2==0, l2)))