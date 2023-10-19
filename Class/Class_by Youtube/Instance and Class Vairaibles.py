class Car:
	wheels = 4## this is the class vairaible which is static and can be called in the class anywhere
	
	def __init__(self): ## init is used to call the arguments passed in it in other methods
		self.mil = 10 ###this two are instace varaible which can be changed for indiviual 
		self.com = 'Audi'


c1= Car()
c2 = Car()

c1.mil = 8  ## updating car milage
Car.wheels = 5  ##this class vairaible can be changed anywhere

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

