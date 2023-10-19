print('''Remember whenever we want to call the class private variable/method in other place
use self.method or variable name \n''')


class myClass:
    def __disp1(self):
        print("This is display1 method")

    def disp2(self):
        print("This is display2 method")
        self.__disp1()

obj=myClass()
obj.disp2()

#obj.disp1() # this will giver error as we r trying to call it outside the call its a private method