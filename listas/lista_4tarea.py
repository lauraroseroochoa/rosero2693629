# programa que de una lista aleatoria 
# suma, promedio, mayor, menor
# ordenar de forma ascendente y descendente
# hallar moda, mediana
# posicion del numero, u cuantas veces esta
import random
lista=[]
tam=int(random.randint(10,20))
print(tam)
if tam%2!=0:
    print("el numero es impar")
else:
    print('el numero es par')
suma=0
cont=0
max_lista=0
min_lista=100000
moda=0


#lista_ordenada=[]
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    cont+=1
    suma+=num
#lista.sort()
    for x in lista:
        if x>max_lista:
         max_lista = x
         print(f"{max_lista} es el numero mayor")
        if i<min_lista and i!=0: 
         min_lista = i
         print(f"{min_lista} es el menor de la lista")
    
    for z in range (len(lista)-1):
        if lista[z]>lista[z+1]:
            j=lista[z]
            lista[z]=lista[z+1]
            lista[z+1]=j
        if len(lista)%2!=0:
            mediana = (lista[(len(lista) //2)-1] + lista[(len(lista)//2)]) / 2
        else:
            mediana= lista[(len(lista)//2)]
   # if lista[i]==lista[i+1]:
      #moda
#for i in lista:
  # if lista[i]==lista[i+1]:
      #moda
#print(moda)
    
promedio=int((suma)/cont)    
print("La lista es",lista)
#print(lista_ordenada)
print("La resultado de la suma es: ",suma)
print("El promedio o media de los elementos de la lista es: ",promedio)

