from Book import *

class Account:

    def __init__(self, name, id):
        self.name=name
        self.__id=id
        self.n_borrowedBooks=[]
        self.n_reservedBooks=[]
        self.n_returnedBooks=[]
        self.n_lostBooks=[]
        self.books=[]
        self.n_lost=0
        self.fineAmount=0
        self.objeto1 = {name : []}
        Book.__init__(self, 'cien años de soledad','gabriel garcia',452125,'01/05/1967', 'laura')

    def claculateFine(self):
        self.fineAmount = (1160000 * 0.3) * self.n_lost
        return int(self.fineAmount)

    def setBorrowed(self,borrowedBooks):
        self.n_borrowedBooks=borrowedBooks

    def getBorrowed(self):
        return self.n_borrowedBooks
    
    def setReserved(self,reservedBooks):
        self.n_reservedBooks=reservedBooks

    def getReserved(self):
        return self.n_reservedBooks
    
    def setReturned(self,returnedBooks):
        self.n_returnedBooks=returnedBooks

    def getReturned(self):
        return self.n_returnedBooks
    
    def setLostBooks(self,n_lostBooks):
        self.n_lostBooks=n_lostBooks

    def getLostBooks(self):
        return self.n_lostBooks
    
    def setFineAmount(self, num):
        self.no_lost = num

    def getFineAmount(self):
        return self.fineAmount
    
    """def  claculateFine(self):
        contador=0
        for i in self.__n_lostBooks:
            contador+=1
            if contador!=0:
                multa= (1600000*0.03)*contador
            return multa"""