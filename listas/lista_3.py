# Lista con un tamaño establecido pero con valores aleatorios
import random 
lista=[] # Se inicia la lista vacia para que se pueda llenar con el random
tam=int(random.randint(10,20)) # Con metodo random se establece el rango del tamaño que debe tener la lista pero de forma aleatoria
print(tam)
for i in range(tam): # Inicio del bloque del ciclo for para que en el rango del tamaño se muestren numeros hasta el 100 de forma aleatria para llenar la lista
    num=int(random.randrange(100))
    lista.append(num) # se agrega cada numero aletoria al final de la lista

print(lista)