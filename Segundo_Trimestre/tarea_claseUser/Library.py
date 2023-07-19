class Library:
    def __init__(self, id:int , title:str):
        self.__id = id
        self.__title = [title]

    def setTitle (self, title):
        if title in self.__title:
            titulo = input("Digita el nuevo titulo: ")
            x = self.__title.index(title)
            self.__title[x] = titulo

    def getTitle (self):
        return self.__title
    
    def agregarLibro (self,isbn,title):
        self.__title.append (title)