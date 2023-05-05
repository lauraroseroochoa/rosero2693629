# programa que de una lista aleatoria 
# suma, promedio 
import random
lista=[]
tam=int(random.randint(10,20))
suma=0
cont=0
max_lista=0
min_lista=100000
moda=0
print(tam)
lista_ordenada=lista.sort(lista)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    cont+=1
    suma+=num
    lista_ordenada=lista.sort(lista)
#for i in lista:
 #   if lista[i]==lista[i+1]:
 #       moda
print(moda)
    
promedio=int((suma)/cont)    
print("La lista es",lista)
print(lista_ordenada)
print("La resultado de la suma es: ",suma)
print("El promedio o medio de los elementos de la lista es: ",promedio)
