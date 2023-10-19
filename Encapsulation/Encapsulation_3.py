class myClass:
    __empid=101

    def getempid(self,eid):
        self.__empid=eid

    def disempid(self):
        print(self.__empid)

obj=myClass()

obj.getempid(105) # this will change the value

obj.disempid() # we are calling the private variable using method

