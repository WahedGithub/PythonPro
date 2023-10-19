##Python will pass object as first implicit argument to EVERY function thats
#part of the class

class Person:
	def __init__(self,name,gender,age,salary):
		self.name = name ## self.vairable will allow to use the vairable in other functions as below show
		self.gender = gender
		self.age = age
		self.salary= salary
		
	def show(self):
		print(self.name, end=" ")
		print(self.gender, end=" ")
		print(self.age, end= " ")
		print(self.salary)## end=" " will not go to new line until print is given, if its given here then the output will be in single line
		

person = Person("amar",'m', 28,35000)
p2= Person("wahed", 'm', 30, 32000)
person.show()
p2.show()
##person -------->
