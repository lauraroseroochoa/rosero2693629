from sys import path
path.append('..\\pythonrosero\\modulos')
#path.append('C:\pythonrosero\modulos')


import SLZ.listas.lista_slz as slz_lista
import SLZ.diccionarios.diccionario_slz as slz_diccio

print (slz_lista.llenarLista(10,20))

diccio={}
x= input('digita la palabra clave: ')
y= input('digita el valor: ')
print(slz_diccio.updateIngles(diccio,x,y))

