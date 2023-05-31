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

def mayor(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(l1)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
            return lista

def mayor(lista):
    mayor=lista[0]
    for num in lista:
        if num>mayor:
            mayor=num
    return mayor

def menor(lista):
    menor=lista[0]
    for num in lista:
        if num<menor:
            menor=num
    return menor

def lisAscendente(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j]<lista[i]:
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista

def lisDescendente(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j]>lista[i]:
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista

def moda(lista):
    frecuencias={}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento]+=1
        else:
            frecuencias[elemento]=1

def moda(lista):
    frecuencias={}
    max_frecuencia=0
    moda=None
    for elemento in lista:
        if elemento not in frecuencias:
            frecuencias[elemento]=1
        else:
            frecuencias[elemento]+=1
        if frecuencias[elemento]>max_frecuencia:
            moda=elemento
            max_frecuencia=frecuencias[elemento]
    return moda

def mediana(lista):
    n=len(lista)
    lista_ordenada=lisAscendente(lista)
    if n % 2==0:
        mediana=(lista_ordenada[n//2 - 1]+lista_ordenada[n//2])/2
    else:
        mediana=lista_ordenada[n//2]
    return mediana

def buscarNum(lista, numero):
    posiciones=[]
    contador=0
    for i in range(len(lista)):
        if lista[i]==numero:
            posiciones.append(i)
            contador+=1
    if contador==0:
        print("El número no se encuentra en la lista")
    else:
        print("El número se encuentra en la posicion:", posiciones)
        print(f"El número aparece {contador}")

# l1=llenarLista(3,10)
# print(l1)

# print("la suma es: ")
# print(sumaLista(l1))

# print("el promedio es: ")
# print(round(promedioLista(l1),2))

# print("el numero mayor es: ")
# print(mayor(l1))

# print("el numero menor es: ")
# print(menor(l1))

# print("la lista organizada de forma ascendente es: ")
# print(lisAscendente(l1))

# print("la lista organizada de forma descendente es: ")
# print(lisDescendente(l1))

# print("la moda es: ")
# print(moda(l1))

# print("la mediana es: ")
# print(mediana(l1))

# num_buscado = int(input("Ingrese el numero que desea buscar: "))
# buscarNum(l1, num_buscado)