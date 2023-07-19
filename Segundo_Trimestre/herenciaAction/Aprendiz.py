# se crea la clase aprendiz que es una subclase de persona y hereda todas sus propiedades mas las propias

from Persona import *
from Curso import *

class Aprendiz(Persona):
    def __init__(self,nombre,documento,formacion,ficha): # se declara el constructor y los atributos que toma de la clase padre y los propios de aprendiz
        Persona.__init__(self,nombre,documento)
        self.__formacion=formacion
        self.__ficha=ficha
        self.__cursos=[] #Se declara cursos con una lista vacia ya quee cada curso se agrega desde afuera
    
    def agregarCurso(self,curso): # Este metodo permite agregar un nuevo curso a la lista vacia declarada en el constructor desde dentro de la clase
        self.__cursos.append(curso) # Nos muestra una relacion por agregacion 
    
    def componerCurso(self): # Este metodo permite agregar un curso a la lista ingresados por teclado 
        nombreCurso=input('Ingrese nombre del curso: ')
        tipoCurso=input('Ingrese tipo del curso: ')
        objcurso=Curso(nombreCurso,tipoCurso) # Tiene dos propiedades de la clase curso
        self.__cursos.append(objcurso) # se agrega el curso a la lsita de cursos 
    
    def verCursos(self): #Este metodo permite visualizar los cursos retornando el valor como un getter
        return self.__cursos