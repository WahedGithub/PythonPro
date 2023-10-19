print("For calling inner call need to define instance variable and under show method")

class Student:
	
	def __init__(self, name, rollno): ## init is used to call the arguments passed in it in other methods
		self.name = name
		self.rollno = rollno
		self.lap= self.Laptop() ##variable need to be declared for inner class access
		

	def show(self):
		print(self.name, self.rollno)
		self.lap.show() # calling the inner class here itself
		
	class Laptop:
		
		def __init__(self):
			self.brand = 'HP'
			self.cpu = 'i5'
			self.ram = '8gb'
			
		def show(self):
			print(self.brand, self.cpu, self.ram)
			
		

s1= Student('Abdul' ,2)
s2= Student('Wahed', 3)

##print(s1.name, s1.rollno)
##print(s1.name +' '+ s2.name, s1.rollno + s2.rollno) instead of this below can be used

s1.show() ##this will help not to call for every employee data
s2.show()