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
    quintil=valor*len(lista)+1/5
    if not len(lista)%5==0:
        quintil=(valor*len(lista)+1/5)=
    mayor=int(quintil)
    menor=int((valor-1)*len(lista)/5)
    if len(lista)>quintil:
        listaquin=lista[menor:mayor]
        return listaquin
    else:
        return f'no se puede hallar el quintil'
    
def hallarCuartiles(lista,valor):
    cuartil=valor*len(lista)/4
    mayor=int(cuartil)
    menor=int((valor-1)*len(lista)/4)
    if len(lista)>cuartil:
        listacuar=lista[menor:mayor]
        return listacuar
    else:
        return f'no se puede hallar el cuartil'


list=llenarLista(50,2.00)
print(list)
print(ordenarListaAsc(list))
print(len(list))
num=int(input('ingresa el quintil a hallar: '))
print(hallarQuintiles(list,num))
num1=int(input('ingresa el cuartil a hallar: '))
print(hallarCuartiles(list,num1))