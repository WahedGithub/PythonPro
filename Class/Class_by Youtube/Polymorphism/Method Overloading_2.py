print("Method Overloading --> is not supported in python but we have different methods to use it though\n")
class Student:
	
	def __int__(self, m1,m2):
		self.m1 =m1
		self.m2 = m2	
	
	def product(a,b):
		p =a*b
		return p
	
	def product(a,b,c):
		p =a*b*c
		return p
		

p1 = Student()

#print(p1.product(1,2,3))
print(p1.product(5,2))
