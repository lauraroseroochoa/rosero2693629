# Se crea la clase curso la cual se relaciona con la clase aprendiz por una agregacion 
class Curso:
    def __init__(self,nombre,tipo): # se crea el constructor con sus atributos
        self.__nombre=nombre
        self.__tipo=tipo

    def getNombre(self): # Metodo para visualizar el nombre del curso
        return self.__nombre