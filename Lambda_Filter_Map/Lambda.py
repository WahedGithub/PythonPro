##lambda(input: expression) lambda is the replacement of function
print("\n\n***********Anonymous or Lambda() Function**********")

s= lambda n:n*n

print ("for calling lambda function just give the vairable name and argument, The Square of n is",s(4))

print("""\n\n Method-2
***********WAP using lambda function**********""")

s= lambda n:n*n
for i in range(1,11):
	print ("The Square of {} is:{}".format(i,s(i)))

print("""\n\n Method-3
***********WAP lambda function with If & else loops**********""")
b = lambda x,y : x if x>y else y
print(b(1,2))