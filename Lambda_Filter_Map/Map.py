##map(expression data, input) map perform operations on all elements
print("""\nMethod-1
********WAP with for squaring a list using map function********""")
l = [1,2,3,4,5]

def squareIT(n):
	return n*n
	
l1= list(map(squareIT, l))
print("square of list using map() is", l1)

print("""\nMethod-2 
********WAP with lambda function********""")
l = [1,2,3,4,5,6]
print("\n********with lambda function defining of function is not required********")
l1= list(map(lambda n: n*n, l)) #with lambda function defining of function is not required
print("square of list using map()+lambda() are",l1)

print("""\nMethod-3 
********WAP with lambda using 2 argument function********""")

l1 = [1,2,3,4,5,]
l2 = [6,7,8,9,10]
print("\n********with lambda function defining of function is not required********")
l3= map(lambda x,y: x*y, l1,l2) #with lambda function defining of function is not required
print("Multiplication of l1 & l2 elements using map()+lambda() are",l3)

print("""\nMethod-4 
********WAP with lambda using 2 argument function with more elements in one list object********""")
l1 = [1,2,3,4,5,] # with more elements its throwing error
l2 = [6,7,8,9,11]
print("\n********if any list is having more elements than other then that will be ignored********")
l3= list(map(lambda x,y: x*y, l1,l2)) #with lambda function defining of function is not required
print("Multiplication of l1 & l2 elements using map()+lambda() are",l3)

print("""\nMethod-5 
********WAP with lambda using 2 argument function********""")
l1 = [1,2,3,4,5,]
l2 = [1,2,3,4,5]
l3 = [1,2,3,4,5]
print("\n********adding three elements and giving the output********")
l4= map(lambda x,y,z: x+y+z, l1,l2,l3) #with lambda function defining of function is not required
print("Addition of l1, l2, l3 elements using map()+lambda() are",l4)

