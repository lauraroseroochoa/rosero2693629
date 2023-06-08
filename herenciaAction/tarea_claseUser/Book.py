class Book:
    def __init__(self,title:str,author:str,isbn:int, publication:str, status):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.publication = publication
        self.duet={title:author}
        self.status = status
        self.comentario={title: None}
    def setTitle(self, title):
        self.title = title
        
    def getTitle(self):
        return self.title
    
    def setAuthor(self, author):
        self.author = author
        
    def getAuthor(self):
        return self.author
    
    def setIsbn(self, isbn):
        self.isbn=isbn
        
    def getIsbn(self):
        return self.isbn
    def setPublication(self, publication):
        self.publication = publication
        
    def getPublication(self):
        return self.publication
    
    def AppendDuet(self,title,author):
        if title in self.duet:
            self.duet.update({self.title: (self.author, author)})
        print (self.duet)
    
    def reservationStatus(self, title):
        if title in self.title:
            return self.status
        
    def feedBack(self,title):
        if title in self.title:
            comentario = input('ingresa el comentario: ')
            self.comentario.update({self.title:comentario})
            print(self.comentario)
            
    """def bookRequest(self,title):
        if title in self.title:
            if Book.reservationStatus(self, title)=='disponible':
                print('libro disponible para reservarlo')
                print('1: reservar')
                print('2: no reservar')
                selector= input('ingresa una opcion')
                match selector:
                    case'1':
                        self.status = 'reservado'
                            return self.status
                    case'2':
                            return 'no reservado"""
    def rewnInformation(self,title):
        return self.title, self.author, self.isbn, self.publication, self.comentario, Book.reservationStatus(self, title)
    
    