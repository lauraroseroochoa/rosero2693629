from Library import *

class Book(Library):
    def __init__(self, title, author, isbn, publication, name):
        self.author = [author]
        self.title = [title]
        self.isbn = isbn
        self.publication = publication
        self.status= "disponible"
        self.information= {title : [author, isbn, publication , self.status] }
        self.duet={title:author}
        self.comentario={title: None}
        self.title1 = {name : title}
        Library.__init__(self, isbn, title)

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
    
    def AddBook (self):
        title = input("Ingresa el titulo del libro: ")
        author = input("Ingresa el autor del libro: ")
        isbn  = input("Ingresa el ISBN del libro: ")
        publication = input ("Escribe la fecha de publicacion: ")
        status = "Disponible"
        self.title.append(title)
        self.author.append(author)
        self.information.update ({title : [author, isbn, publication , status]})
        Library.agregarLibro (self, isbn, title)
        return self._information
    
    def book1(self,name:str, libro:str):
        values = list(self.title1.values())
        for i in values:
            values = i
        del self.title1[name]
        self.title1.update({name : [values] + [libro]})
        return self.title1
    
    def AppendDuet(self,title,author):
        if title in self.duet:
            self.duet.update({self.title: (self.author, author)})
        print (self.duet)
    
    def reservationStatus(self, title):
        if title in self.title:
            return self.status
        
    def feedBack(self,title):
        if title in self.title:
            comentario = input('ingresa el comentario para este libro: ')
            self.comentario.update ({title : comentario})
            print(self.comentario)
            
    def bookRequest(self,title):
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
                        return 'no reservado'
                    
    def rewnInformation(self,title):
        return self.title, self.author, self.isbn, self.publication, self.comentario, Book.reservationStatus(self, title)
       