# Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:
# Cuál de los dos tiene la suma más alta
# Cuál de los dos tiene el número mayor
# Cuál de los dos tiene el número menor
# Cuál es el promedio conjunto (uniendo los dos arreglos)
# Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
# Cuál de los dos tiene mayor cantidad de pares
# Cuál de los dos tiene mayor cantidad de impares
import random
def llenarlista_1(tam,rango):
    lista_1=[random.randrange(rango) for i in range(tam)]
    return lista_1

def llenarlista_2(tam,rango):
    lista_2=[random.randrange(rango) for i in range(tam)]
    return lista_2

def sumaListas(lista_1,lista_2):
    sum1=0
    sum2=0
    for x in range(len(lista_1)):
        sum1+=lista_1[x]
    for j in range(len(lista_2)):
        sum2+=lista_2[j]

    print('la suma de la primer lista es:', sum1)
    print('la suma de la segunda lista es:', sum2)
    if sum1 > sum2:
        return 'la suma de la primer lista es la mas alta '
    elif sum1 < sum2:
        return 'la suma de la segunda lista es la mas alta'
    else:
        return 'las dos listas tienen la misma suma' 

def numMayorListas(lista_1,lista_2):
    max_lista1=0
    max_lista2=0
    for i in lista_1:
        if i>max_lista1:
         max_lista1 = i

    for z in lista_2:
        if z>max_lista2:
         max_lista2 = z

    if max_lista1 == max_lista2:
        print("Ambas listas tienen el mismo número mayor:", max_lista1)
    elif max_lista1 > max_lista2:
        print("La lista 1 tiene el número mayor:", max_lista1)
    else:
        print("La lista 2 tiene el número mayor:", max_lista2)
    


def numMenorListas(lista_1,lista_2):
    min_lista1=10000
    min_lista2=10000
    for i in lista_1:
        if i<min_lista1 and i!=0: 
         min_lista1 = i
    for f in lista_2:
        if f<min_lista2 and f!=0: 
         min_lista2 = f
    if min_lista1 == min_lista2:
        print("Ambas listas tienen el mismo número menor:", min_lista1)
    elif min_lista1 < min_lista2:
        print("La lista 1 tiene el número menor:", min_lista1)
    else:
        print("La lista 2 tiene el número menor:", min_lista2)

def sumaLista1(lista_1):
    sum1=0
    for x in range(len(lista_1)):
        sum1+=lista_1[x]
    return sum1

def promLista1(lista_1):
    return sumaLista1(lista_1)/len(lista_1)

def sumaLista2(lista_2):
    sum2=0
    for x in range(len(lista_2)):
        sum2+=lista_2[x]
    return sum2

def promLista2(lista_2):
    return sumaLista2(lista_2)/len(lista_2)

def unir_listas(lista_1, lista_2):
    lista_1.extend(lista_2)
    return lista_1


def sumarLista(lista_1):
    sum=0
    for c in lista_1:
        sum+=c
    return sum


def promedioLista(lista):
    return sumarLista(lista)/len(lista)

def paresImpares(lista_1, lista_2):
    pares_lista1 = 0
    impares_lista1 = 0
    pares_lista2 = 0
    impares_lista2 = 0

    for num in lista_1:
        if num % 2 == 0:
            pares_lista1 += 1
        else:
            impares_lista1 += 1

    for num in lista_2:
        if num % 2 == 0:
            pares_lista2 += 1
        else:
            impares_lista2 += 1


    print(f"la lista uno tiene {pares_lista1} pares y {impares_lista1} impares")

    print(f"la lista dos tiene {pares_lista2} pares y {impares_lista2} impares")

lista_1=llenarlista_1(10,30)
lista_2=llenarlista_2(10,30)
print (lista_1)
print (lista_2)
print (sumaListas(lista_1,lista_2))
print(numMayorListas(lista_1,lista_2))
print(numMenorListas(lista_1,lista_2))
print(sumaLista1(lista_1))
print(promLista1(lista_1))
print(sumaLista2(lista_2))
print(promLista2(lista_2))

print(paresImpares(lista_1, lista_2))
lista_1=unir_listas(lista_1,lista_2)
print(sumarLista(lista_1))
print("La lista unida es: ",lista_1)

print("el promedio conjunto es: ")
print(round(promedioLista(lista_1),2))