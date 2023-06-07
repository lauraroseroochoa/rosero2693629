class Account:
    def __int__(self,n_borrowedBooks,n_reservedBooks,n_returnedBooks,n_lostBooks,fineAmount):
        self.__n_borrowedBooks=n_borrowedBooks
        self.__n_reservedBooks=n_reservedBooks
        self.__n_returnedBooks=n_returnedBooks
        self.__n_lostBooks=n_lostBooks
        self.__fineAmount=fineAmount

    def claculateFine(self):
        pass

    def setBorrowed(self,n_borrowedBooks):
        self.__n_borrowedBooks

    def getBorrowed(self):
        return self.__n_borrowedBooks
    
    def setReserved(self,n_reservedBooks):
        self.__n_reservedBooks=n_reservedBooks

    def getReserved(self):
        return self.__n_reservedBooks
    
    def setReturned(self,n_returnedBooks):
        self.__n_returnedBooks=n_returnedBooks

    def getReturned(self):
        return self.__n_returnedBooks
    
    def setLostBooks(self,n_lostBooks):
        self.__n_lostBooks=n_lostBooks

    def getLostBooks(self):
        return self.__n_lostBooks
    
    def setFineAmount(self,fineAmount):
        self.__fineAmount=fineAmount

    def getFineAmount(self):
        return self.__fineAmount
    