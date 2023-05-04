# programa que de una lista aleatoria 
# suma, promedio 
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
    
promedio=int((suma)/cont)    
print("La lista es",lista)
print("La resultado de la suma es: ",suma)
print("El promedio de los elementos de la listaes: ",promedio)
