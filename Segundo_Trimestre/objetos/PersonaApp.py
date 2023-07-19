from Persona import *
objeto=Persona('laura',1074809501)

objeto.setNombre('Tatiana')

objeto.setDocumento(107480520)

print(objeto.getNombre())
print(objeto.getDocumento())

x=1
while x!='0':
    x=input('digita un curso: ')
    if x!='0':
        objeto.AñadirCursos(x)
        

y=input('ingresa el curso a modificar: ')
cursonuevo=input('ingresa el nuevo nombre:' ) 
objeto.ModificarCursos(y,cursonuevo)

cursoEliminar=input('ingresa el curso que quieres eliminar: ')
objeto.EliminarCursos(cursoEliminar)

print(objeto.ConsultarCursos())