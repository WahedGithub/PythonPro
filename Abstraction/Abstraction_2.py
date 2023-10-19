from abc import ABC, abstractmethod
class Animal(ABC): ## now A is abstract class coz ABC is the abstract pre defined class
    @abstractmethod
    def eat(self):
        pass## or None can also be used

class Tiger(Animal):
    def eat(self):
        print("eat non-Veg")

class Cow(Animal):
    def eat(self):
        print("eat Veg")

t= Tiger()
c= Cow()
t.eat()
c.eat()