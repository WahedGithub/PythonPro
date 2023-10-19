print('Classes allow us to group our data & functions in a way thats easy to reuse and also build upon if need to be')

print('\nMethods are nothing but a function associated with a class\n')

print("\n instance varaible--> unique variable containing different value/number\n")

print ('\n constructor is the one who assign the memory in the class')

print('''class variable-->we can either define under class by giving class name.variable name or can def a function 
for same and this can be called/used in whole program''')

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
print(Employee.fullname(emp_1))#this is another way of calling the method

emp_2.fullname()##print need to be given as this is method not function

