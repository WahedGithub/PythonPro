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

print(emp_2.fullname())
print(Employee.fullname(emp_1))

emp_2.fullname()##print need to be given as this is method not function