# desde este archivo se realiza la aplicacion de los metodos
from Aprendiz import *
from Curso import *

objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629) # se instacia un objeto de la clase aprendiz que por herencia tambien pertenece a la clase persona
#print(objeto.__dict__)
objcurso=Curso("Programacion Software","tecnico") # se instancia un objeto de la clase curso 
objeto.agregarCurso(objcurso)# se agrega el objeto que se instancio en la linea anterior de la clase curso a la lista vacia de cursos
#print(objeto.__dict__)
objeto.componerCurso() # se agrega un  curso con sus atributos por composicion ya que se hace desde un metodo la misma clase aprendiz
objeto.componerCurso() # se agrega un  curso con sus atributos por composicion ya que se hace desde un metodo la misma clase aprendiz
#print(objeto.verCursos())

#  con el for y el metodo de ver cursos la variable cursito mostrara el nombre (getnombre) del curso ingresado anteriormente por composicion
for cursito in objeto.verCursos():
    print(cursito.getNombre())