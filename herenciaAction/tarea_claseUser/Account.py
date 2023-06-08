class Account:
    def __int__(self,n_borrowedBooks,n_reservedBooks,n_returnedBooks):
        self.n_borrowedBooks=n_borrowedBooks
        self.n_reservedBooks=n_reservedBooks
        self.n_returnedBooks=n_returnedBooks
        self.n_lostBooks=[]
        self.fineAmount=0

    def claculateFine(self):
        pass

    def setBorrowed(self,n_borrowedBooks):
        self.n_borrowedBooks

    def getBorrowed(self):
        return self.n_borrowedBooks
    
    def setReserved(self,n_reservedBooks):
        self.n_reservedBooks=n_reservedBooks

    def getReserved(self):
        return self.n_reservedBooks
    
    def setReturned(self,n_returnedBooks):
        self.n_returnedBooks=n_returnedBooks

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
                
    