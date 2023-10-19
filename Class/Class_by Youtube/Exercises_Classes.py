class Myclass:
	x= 5
	
print(Myclass)

p= Myclass
print(p.x)

print("\n****Second class program with method*****\n")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print( p1.age)

print("\n****Third class program with method and first parameter explanation*****\n")
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print("\n****fourth class program with method on deleting and modifying the variables*****\n")
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
print(p1.age)
p1.age=40
print("updated age is :",p1.age)
#del p1.age ##this will delete the age
#print(p1.age)
#del p1 ## this will delete the p1 object
#print(p1.name, p1.age)
