print("\nMethod Overriding--> Is the same way like using def show in inheritance first it will check for child class else it will go to parent class\n")

class A:
	
	def show(self):
		print("in A Show")
		
class B(A):
	
	def show(self):
		print("in B  Show")
	

		
a1 = B()
a1.show()

print("\n2nd example--> dont have to define show here\n")
class C:
	
	def show(self):
		print("in C Show")
		
class D(C):
		None #or pass
	

c1 = D()
c1.show()