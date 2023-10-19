class Employee:
    def __init__(self, first, last,pay):#Self will be taken as class name when we pass the arguments for multiple employee's
	    self.first = first
            self.last = last
            self.pay = pay
            self.email= first + '.' + last + '@company.com'

>>> emp_1=Employee('Abdul', 'Wahed', 20000)
>>> emp_2=Employee('Suresh', 'Rajesh', 30000)
>>> 
>>> print(emp_1.email)
