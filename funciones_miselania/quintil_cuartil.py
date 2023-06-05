# minimo 15 maximo 125.{validación} Incluir todos los numeros
#Llenar lista {Estaturas. 1,50 - 2,00} - función
# hacer una función que encuentre todos los cuartiles y otra función para todos los quintiles
# Hallar cuadriles y quintiles (impriman los percentiles en rango)

import random
def llenarLista(tam,rango):
    tam1=random.randint(15,tam)
    lista=[round(random.uniform(1.50,rango),2) for i in range(tam)]
    return lista
        
def ordenarListaAsc(lista):
    for i in range(len(lista)):
        for j in range(i+1,(len(lista))):
         if lista[i]>lista[j]:
             aux=lista[i]
             lista[i]=lista[j]
             lista[j]=aux
    return lista  

def hallarQuintiles(lista,valor):
    quintil=int(valor*len(lista)+1/5)
    print(quintil)
    if len(lista)%5!=0:
        x=lista.pop(quintil)
        y=lista.pop(quintil+1)
        lista.insert(quintil, x)
        lista.insert(quintil+1, y)
        z=round(x+y/2,2)
        return z
    else:
        quintil=int(valor*len(lista)/5)
        mayor=int(quintil)
        menor=int((valor-1)*len(lista)/5)
        listaquin=lista[menor:mayor]
        return listaquin

    
def hallarCuartiles(lista,valor):
    cuartil=int(valor*len(lista)/4)
    print(cuartil)
    if len(lista)%4!=0:
        x=lista.pop(cuartil)
        y=lista.pop(cuartil+1)
        lista.insert(cuartil, x)
        lista.insert(cuartil+1, y)
        z=round(x+y/2,2)
        return z
    else:
        cuartil=int(valor*len(lista)/4)
        mayor=int(cuartil)
        menor=int((valor-1)*len(lista)/4)
        listaquin=lista[menor:mayor]
        return listaquin


list=llenarLista(50,2.00)
print(list)
print('lista ordenada','\n',ordenarListaAsc(list))
print('longitud de la lista',len(list))
num=int(input('ingresa el quintil a hallar: '))
print(hallarQuintiles(list,num))
num1=int(input('ingresa el cuartil a hallar: '))
print(hallarCuartiles(list,num1))