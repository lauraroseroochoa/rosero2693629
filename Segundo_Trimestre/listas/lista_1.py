# suma, promedio, max y min de la lista 
import random
lista=[]
tam=int(random.randint(10,20))
suma=0
cont=0
max_lista=0
min_lista=100000
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    cont+=1
    suma+=num
    if num>max_lista: # identificar si el numero ingresado es mayor que cero
      max_lista = num
    if num<min_lista and num!=0: # identificar que el numero es menor del que se le asigno 
      min_lista = num
promedio=int((suma)/cont)    
print("La lista es",lista)
print("La resultado de la suma es: ",suma)
print("El promedio de los elementos de la listaes: ",promedio)
print("El maximo de la lista es: ",max_lista)
print("El minimo de la lista es: ",min_lista)
    