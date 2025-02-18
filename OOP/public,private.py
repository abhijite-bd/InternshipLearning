class Bank:
    def __init__(self):
        print("Ac created")
    def setname(self,name):
        self.name=name  #public name
    def setno(self,no):
        self.__no=no  #private data
    def __setpass(self,passw):   #private pass
        self.__pass=passw
    def getDetails(self):
        print(self.name,self.__no,self.__pass)
    def reset(self,passw):
        self.__setpass(passw)
b1=Bank()
b1.setname("man1")
b1.setno("abcde")
b1.reset("1234")
print(b1.name) #possible
# print(b1.no)    #impossible bcz private
b1.getDetails()