import re
class Poem:
	def __init__(self):             ##by default self object will be given with init
		self.lines = []         #just lines = [] make its a local vairable add slef.lines to make it global
		fobj = open("poem.txt", "r")
		for line in fobj:
			self.lines.append(line.strip())
			
	def clean(self): ##One way to remove the special characters with regular exp
		pat = '[^A-Za-z0-9 ]' ##here ^ should be given and after 9 space is required
		for index,line in enumerate(self.lines):
			self.lines[index] = re.sub(pat, '', line)
			
	def clean(self): ##Other way to remove the special characters with lambda and map
		pat = '[^A-Za-z0-9 ]'
		f = lambda line:re.sub(pat, '',line)
		self.lines = list(map(f,self.lines))
			
	def show(self):
	    for line in self.lines:
                print(line)
            print()
            
            
if __name__ == '__main__':
    p1= Poem()
    p1.show() ##Show is to call the function
