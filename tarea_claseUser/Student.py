from User import *

class Student(User):
    def __init__(self,clase):
        self.__clase = clase
        
    def setClase(self, clase):
        self.__clase = clase
        
    def getClase(self):
        return self.__clase
    
