import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)


def numMayorLista(lista):
    max_lista=0
    for i in lista:
        if i>max_lista:
         max_lista = i
    return max_lista

def numMenorLista(lista):
    min_lista=10000
    for i in lista:
        if i<min_lista and i!=0: 
         min_lista = i
    return min_lista
     
def ordenarListaAsc(lista):
    for i in range(len(lista)):
        for j in range(i+1,(len(lista))):
         if lista[i]>lista[j]:
             aux=lista[i]
             lista[i]=lista[j]
             lista[j]=aux
    return lista  


def ordenarListaDesc(lista):
    for i in range(len(lista)):
        for j in range(i+1,(len(lista))):
         if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux     
    return lista  

def moda_lista(lista):
    num=0
    for i in lista:
        cont=0
        for b in lista:
            if i==b:
                cont+=1
        if cont>num:
            num=cont
            moda=i
    return moda
            

def mediana_lista(lista):
    for i in range (len(lista)):
        if len(lista)%2==0:
            mediana = (lista[(len(lista) //2)-1] + lista[(len(lista)//2)]) / 2
        else:
            mediana= lista[(len(lista)//2)]
        return mediana
#def posicion_lista(lista):
    
#def buscar_lista(lista):

l1=llenarLista(15,15)
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2))
print(numMayorLista(l1))
print(numMenorLista(l1))
print(ordenarListaAsc(l1))
print(ordenarListaDesc(l1))
print(moda_lista(l1))
print(mediana_lista(l1))
