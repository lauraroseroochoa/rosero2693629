from Book import *
from Account import *

class User(Account):    
    def __init__(self, name,id):
        self.__name = name
        self.__id = id
        self.__registrado = None
        Account.__init__(self, name, id)
        Book.__init__(self, 'cien años de soledad','gabriel garcia',452125,'01/05/1967', 'laura')
        
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
            self.__registrado = "Registrado"
            return "Registrado"
        else:
            self.__registrado = "No registrado"
            return "No Registrado"
            
    def checkAccount(self, name):
        return self.objeto1[name]
    
    def reservedBook(self ,name, title):
        self.n_reservedBooks.append(title)
        self.books.append (title)
        del self.objeto1[name]
        self.objeto1.update ({name : self.books + [title]})
        Book.book1(self,name,title)
        
    def returnedBook (self, name, title):
        self.n_returnedBooks.append(title)
        self.books.append(title)
        del self.objeto1[name]
        self.objeto1.update ({name : self.books + [title]})
        Book.book1(self,name,title)
        
    def lostBook(self, name, title):
        self.n_lostBooks.append(title)
        self.books.append (title)
        del self.objeto1[name]
        self.objeto1.update ({name : self.books + [title]})
        Book.book1(self,name,title)
        self.setFineAmount(len(self.n_lostBooks))


    
    def getInfoBook(self, title, information):
        self.__information = information
        print(self.__information[title])
            
        
    #def agregarCurso(self,title):
        #pass self.__clase.append(title)