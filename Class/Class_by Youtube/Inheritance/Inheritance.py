print ("\n********Class A() is a Super/parent class**********\n")

class A:
	def feature1(self):
		print("Feature 1 Working")
		
	def feature2(self):
		print("Feature 2 Working")
		
print ("\n********Class B() is a Sub/child class of A() & this is called Single level inheritance**********\n")

class B(A):
	def feature3(self):
		print("Feature 3 Working")
		
	def feature4(self):
		print("Feature 4 Working")
		
print ("\n********Class C() is a Sub/child class of B& A() & this is called Multi level inheritance**********\n")	
class C(B):
	def feature5(self):
		print("Feature 5 Working")
		
		
a1= A()

a1.feature1()
a1.feature2()
b1 = B()
print("\nClass B(A) Single Level inheritance")
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
print("\nClass C(B(A)) Multi Level inheritance")
c1= C()
c1.feature4()
c1.feature5()
c1.feature1()