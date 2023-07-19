from sys import path

path.append('..\\pythonrosero\\modulos')

import MABE.Diccionario.funtion as mabediccio
import MABE.Listas.funcion as mabelista

diccio={}
print(mabediccio.alimentar_diccionario_esp_ingles(diccio))
print(mabelista.llenarLista(10,20))