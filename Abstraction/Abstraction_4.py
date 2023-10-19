from abc import ABC, abstractmethod
class Cal(ABC):
    def __init__(self,value):
        self.value =value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class B(Cal):
    def add(self):
        print(self.value + 100)

    def sub(self):
        print(self.value - 10)

cobj= B(100)
cobj.add()
cobj.sub()