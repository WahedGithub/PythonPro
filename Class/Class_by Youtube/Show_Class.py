class Employee:
	
	def __init__(self, first, last, pay): # self is used in constructor to reuse for multiple employee's and after self we can pass the attributes
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		
	def show(self):
		print(self.first, self.last, self.pay)
		
emp_1 = Employee('Abdul', 'Wahed', 20000)
emp_2 = Employee('Test', 'User', 30000)

print(emp_1.first, emp_1.last)
print(emp_2.first)

print(emp_1.email)
print(emp_2.email)

print("show k kamaal")
emp_1.show()

		