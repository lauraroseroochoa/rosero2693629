# tamaño lista de 15 y 20
# datos dentro de  la lista de 0 a 9
# decir si esta
# decir si esta repetido
# decir si esta repetido cuantas veces esta

import random
num1=1
suma=0
repetidos=[]

lista=[(random.randrange(9))for i in range(random.randint(15,20))]
print(lista)

while num1<=9:
    num1= int(input('ingrese un numero: '))
    cont=0
    if num1 in lista: # el operador in me dice si un elemento esta en la lista  
        print('el numero esta en la lista')
    else:
        print('el numero no esta en la lista')
    """for x in lista:
        if num1 in lista:
            sum+=1"""
    for b in lista:
        if b == num1:
            cont+=1
            for x in range(len(lista)):
                repetidos.append(x)

    if cont>=2:
        print('el numero esta repetido')
        print("numero repetido esta cantidad de veces:")
        break
print(cont)
