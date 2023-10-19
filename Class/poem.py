class Poem:
	def __init__(self):             ##by default self object will be given with init
		self.lines = []         #just lines = [] make its a local vairable add self.lines to make it global
		fobj = open("poem.txt", "r")
		for line in fobj:
			self.lines.append(line.strip())

	def show(self):
		for line in self.lines:
			print(line)
			
p1= Poem()
p1.show()
