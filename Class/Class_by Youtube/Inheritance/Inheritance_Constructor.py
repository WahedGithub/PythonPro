class A:

	def __init__(self): ## if there is no init defined in class B then it will call for init of A
		print("in A init")
		
	def feature1(self):
		print("Feature 1 Working")
		
	def feature2(self):
		print("Feature 2 Working")
		
print ('''\n********Class B() is a Sub/child class of A() & this is called Single level inheritance
2. And this is also a Method Overidding**********\n''')

class B(A):

	def __init__(self):	# if init is present in class B then it will not call for init of A
	#The child's __init__() function overrides the inheritance of the parent's __init__() function, To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
		print("in B init")
		#super().__init__(self) # this is to call super class init but here its not working 
		#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
		#print("in B init")
		
	def feature3(self):
		print("Feature 3 Working")
		
	def feature4(self):
		print("Feature 4 Working")
		
a1 = B()