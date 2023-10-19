class Student():
	school = "School"
	
	def __init__(self, m1,m2,m3):
		self.m1 =m1
		self.m2 = m2
		self.m3 = m3
		
	def avg(self): ## if we are working for instance and use 'self'
		return (self.m1 + self.m2 + self.m3)/3
		
	@classmethod ## to define a class method use this @classmethod
	def info(cls): # if we are working for class use 'cls'
		return cls.school
		
	@staticmethod # this is to define static method 
	def stat():
		print("This is Student class.. in abc module")

	
s1 = Student(34,47,32)

print ('This is average of student', s1.avg())
print (Student.info())
print('This is average of student',Student.stat())