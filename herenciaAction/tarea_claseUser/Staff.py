from User import *

class Staff(User):
    
    def __init__(self,dept):
        self.__dept = dept
        
    def setDept(self,dept):
        self.__dept = dept
        
    def getDept(self):
         return self.__dept
     