import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    suma=0
    for x in lista:
        suma+=x
    return suma

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayor(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def menor(lista):
    menor=100000000
    for i in lista:
        if i<menor:
            menor=i
    return menor

def ordenAscen(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

def ordenDesce(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

def modaLista(lista):
    ind=0
    for i in lista:
        cont=0
        for f in lista:
            if i==f:
                cont+=1
        if cont>ind:
            ind =cont
            moda=i
    return moda

def medianaLista(lista):
    if len(lista)%2==0:
        mediana=(lista[(len(lista)//2)-1]+ lista[len(lista)//2])/2
    else:
        mediana =lista[(len(lista)//2)]
    return mediana


def buscarLista(lista,x):
    cont=0
    if x in lista:
        for i in range(len(lista)):
            if x==lista[i]:
                cont+=1
        return f"El numero existe {cont} veces"
    else:
        return "El numero no existe"