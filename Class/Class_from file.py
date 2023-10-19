class Person:
	def __init__(self,name,gender,age,salary):
		self.name = name
		self.gender = gender
		self.age = age
		self.salary= salary
		
	def show(self):
		print(self.name, end=" ")
		print(self.gender, end=" ")
		print(self.age, end= " ")
		print(self.salary)

fobj = open("class.txt", "r")
persons = []# this will create empty list

for line in fobj:
    name,gender,age,salary = line.split()
    person = Person(name,gender,age,salary)
    persons.append(person)


for person in persons:
    person.show()

    
