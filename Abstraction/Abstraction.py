# ABC is the pre defined abstract class in python
#abstractmethod also comes from abc

print ('''1. Main class body should not contain anything and main class object cannot be 
created for printing
2. Another sub class(inheritance) must be created and object must be assigned to the same.
3. This is used when we know the requirement but implementation is not clear then we can use this method
and later stages create the classes as per the implementation and use the same\n''')

from abc import ABC, abstractmethod
class A(ABC): ## now A is abstract class coz ABC is the abstract pre defined class
    @abstractmethod
    def display(self):
        None## or pass can be given

class B(A):
    def display(self):
        print("Program output: this is display Method")

obj= B()
obj.display()