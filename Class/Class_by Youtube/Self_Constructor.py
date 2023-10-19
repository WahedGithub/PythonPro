class Computer:
	
	def __init__(self): ## init is used to call the arguments passed in it in other methods
		self.Name = "Wahed"
		self.age = 28

	def compare(self,other): #compare(self, the one which need to be compared
		if self.age == other.age:
			return True
		else:
			return False


#b = lambda c1.age,c2.age : print("they are same") if c1=c2 else print("They are Diff") ##This can also be used instead of above thing have to look upon

c1= Computer()
c1.age = 29
c2 = Computer()

if c1.compare(c2):
	print("They are Same")
else:
	print("They are Different")


print(c1.Name)
print(c2.Name)

