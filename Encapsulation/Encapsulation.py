print('''1. In an OOPs program, you can restrict access to methods and variables
2. This can prevent the data from being modified by accident and is known as encapsulation
3. Encapsulation can be achieved using private variables & private methods\n''')

class myClass:
    __a=10 # now this has become private variable & its not accessible from outside the class

    def disp(self):
        print(self.__a) # here we have to define the with self coz variable is defined inside the class


obj= myClass()
obj.disp()

#print(myClass.__a) # we cannot access coz its private variable

