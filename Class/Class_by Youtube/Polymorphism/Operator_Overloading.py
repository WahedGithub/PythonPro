print ('''Operator Overloading is one of the method in PolyMorphism -- Poly = Many, Morph = from

1. You can change the meaning of an operator in Python depending upon the operands used. 
This practice is known as operating overloading.
2. Python operators work for built-in classes. But same operator behaves differently with different types. 
For example, the + operator will, perform arithmetic addition on two numbers, merge two lists and 
concatenate two strings.

3. This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading.

4. So what happens when we use them with objects of a user-defined class? Let us consider the following 
class, which tries to simulate a point in 2-D coordinate system.
''')

class Point:
	def __init__(self, x, y):
		self.x=x
		self.y= y
	
	def __str__(self): #define this str method to control printing
		return "{0},{1}".format(self.x, self.y)
		
	def __add__(self,other):
		x= self.x + other.x
		y= self.y + other.y
		return Point(x,y)
		
		
p1 = Point(2,3)
p2= Point(-1,2)
#p1 + p2 ## this will give unsupported operands error

print(p1) ## this will print the class instance.
print(str(p1))
print(format(p2))
print(p1+p2)# "p1(x)+ p2(x), p1(y)+p2(y):", p1 + p2)

print('''So, when you do str(p1) or format(p1), Python is internally doing p1.__str__(). Hence the name, special functions.

Ok, now back to operator overloading.

What actually happens is that, when you do p1 + p2, Python will call p1.__add__(p2) which in turn is 
Point.__add__(p1,p2). Similarly, we can overload other operators as well. 
The special function that we need to implement is tabulated below.''')





