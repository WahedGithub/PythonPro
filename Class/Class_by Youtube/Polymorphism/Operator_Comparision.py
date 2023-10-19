print('''\nOverloading Comparison Operators in Python
1. Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.

2. Suppose, we wanted to implement the less than symbol < symbol in our Point class.

3. Let us compare the magnitude of these points from the origin and return the result for this purpose. It can be implemented as follows.''')

class Point():
	def __init__(self, x =0, y = 0):
		self.x =x
		self.y= y
		
	def __str__(self):
		return "({0},{1})".format(self.x, self.y)
		
	def __It__(self, other):
		self_mag = (self.x**2) + (self.y **2)
		other_mag=  (other.x**2) + (other.y**2)
		return self_mag < other_mag

Point(1,1) < Point(-2,-3)
Point(1,1) < Point(1,1)
		