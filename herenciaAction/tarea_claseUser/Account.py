class Account:

    def __init__(self,borrowedBooks:int,reservedBooks:int,returnedBooks:int):
        self.n_borrowedBooks=borrowedBooks
        self.n_reservedBooks=reservedBooks
        self.n_returnedBooks=returnedBooks
        self.n_lostBooks=[]
        self.fineAmount=0

    def claculateFine(self):
        pass

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
    
    def setFineAmount(self,fineAmount):
        self.fineAmount=fineAmount

    def getFineAmount(self):
        return self.fineAmount
    
    def  claculateFine(self):
        contador=0
        for i in self.__n_lostBooks:
            contador+=1
            if contador!=0:
                multa= (1600000*0.03)*contador
            return multa
                
    