print("***********this is from this link https://www.youtube.com/watch?v=qiSCMNBIP2g ************")

class Computer:
	
	def config(self): 
		print("i5, 16gb, 1TB")
		
a ='8'
print(type(a))

com1 = Computer()
print(type(com1))

com2= Computer()

print("/n*********this is one method of calling the class*********")
Computer.config(com1) ## this is one method of calling the class

print("/n*********this is another method and most useable method of calling the class*********")
com1.config()
com2.config()
