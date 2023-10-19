class Computer:
	def __init__(self, cpu, ram): ## init is used to call the arguments passed in it in other methods
		self.cpu = cpu
		self.ram = ram

	
	def config(self): 
		print("config is", self.cpu, self.ram)
		
com1= Computer("i5", 16)
com2 = Computer('Lenovo 5', 8)

com1.config()
com2.config()