print('''\n1. Classes allow us to group our data & functions in a way thats easy to reuse and also build upon if need to be')

2. Methods are nothing but a function associated with a class

3. instance varaible--> unique variable containing different value/number

4. constructor is the one who assign the memory in the class

5. Python is an object oriented programming language.

6. Almost everything in Python is an object, with its properties and methods.

7. A Class is like an object constructor, or a "blueprint" for creating objects.

8. We can think of class as a sketch (prototype) of a house. 
It contains all the details about the floors, doors, windows etc. 
Based on these descriptions we build the house. House is the object.

9. As, many houses can be made from a description, we can create many objects from a class. 
An object is also called an instance of a class and the process of creating this object is called instantiation.

10. class variable-->we can either define under class by giving class name.variable name or can def a function 
for same and this can be called/used in whole program\n''')

class Employee:
	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	def fullname(self): ## this is a method not a function so have to give self
		return '{} {}'.format(self.first, self.last)
		
emp_1 = Employee('Abdul', 'Wahed', 20000)
emp_2 = Employee('Ramesh', 'Suresh', 30000)

#print(emp_1.email)
#print(emp_2.email)

print(emp_2.fullname())# without print we can't able to call any thing in class like below
print(Employee.fullname(emp_1), emp_1.pay)#this is another way of calling the method

emp_2.fullname()##print need to be given as this is method not function

