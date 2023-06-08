# super clase

from Book import *
from Account import *
class User:
    
    def __init__(self, name,id):
        self.__name = name
        self.__id = id
        
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setId(self, id):
        self.__id = id
        
    def getId(self):
        return self.id
    
    def Verify(self, name, id):
        if name == self.__name and id==self.__id:
            print('registrado')
            
        else:
            print('no estas registrado')
            
    def checkAccount(self, name,id):
        if User.Verify(self, name, id)=='registrado':
            return Account.getBorrowed(), Account.getReserved(), Account.getReturned()
    
    def getInfoBook(self, name, id):
            
        pass
        
    #def agregarCurso(self,title):
        #pass self.__clase.append(title)