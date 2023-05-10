# Las listas pueden ser utilizadas como parametros de una funcion 
# Definir una funcion para llenar una lista de forma aletoria
import random
def llenarLista(tam,rango): # En los parametros escribimos el rango y tamaño de la lista
    lista=[random.randrange(rango) for i in range(tam)]    # Para llenar la lista aleatoria con random y asi asignando el valor de los argumentos aleatorios para cada parametro
    return lista # La palabra retorno termina la ejecucion de la funcion y el usuario decide que hacer con este resultado
 # Esta funcion realiza la suma de los elementos aleatorios de la lista
def sumaLista(lista): # Dentro la definion de una funcion se puede usar la lista declarada en la funcion anterior
    sum=0
    for x in lista:
        sum+=x
    return sum # Se retorna la suma para que se decida que hacer con e resultado
# esta funcion permite obtener el promedio de la lista teniendo en cuenta la funcion suma lista 
def promedioLista(lista):
    return sumaLista(lista)/len(lista) # el retorno de la funcion es la funcion de sumar la lista dividido entre la longitud de la lista

l1=llenarLista(3,10)
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2)) # muestra solo dos digitos decimales
