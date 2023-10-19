from abc import ABC, abstractmethod
class X(ABC): ## now A is abstract class coz ABC is the abstract pre defined class
    @abstractmethod
    def m1(self):
        pass## or None can also be used

    @abstractmethod
    def m2(self):
        None  ## or None can also be used

class Y(X):
    def m1(self):
        print("This is m1")
##either we can create another method inside Y class or another class like below can be created with only m2 method

class Z(Y):
    def m2(self):
        print("This is m2")

zobj= Z()
zobj.m1()
zobj.m2()



