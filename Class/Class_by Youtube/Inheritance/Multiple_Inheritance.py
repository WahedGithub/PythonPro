class A(object):
	def __init__(self):
		self.str1= "Abdul"
		print("A")

class B(object):
	def __init__(self):
		self.str2= "Wahed"
		print("B")

print(" \n*************This is multiple inheritance***********\n")
class C(A, B): ## here we are calling both A & B class
	def __init__(self):
		A.__init__(self)
		B.__init__(self)
		print("C")
	#this is to print the strings	
	def printstrs(self):
		print(self.str1, self.str2)
		

ob = C()
ob.printstrs()
ob.
	