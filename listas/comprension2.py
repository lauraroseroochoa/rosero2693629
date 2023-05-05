# tamaño lista de 15 y 20
# datos dentro de  la lista de 0 a 9
# decir si esta
# decir si esta repetido
# decir si esta repetido cuantas veces esta

import random
num1=1
suma=0
#num1= int(input('ingrese un numero'))
lista=[(random.randrange(9))for i in range (random.randint(15,20))]
print(lista)
repetidos=[]
while num1<=9:
    num1= int(input('ingrese un numero: '))
    if num1 in lista: # el operador in me dice si un elemento esta en la lista  
        print('el numero esta en la lista')
    else:
        print('el numero no esta en la lista')
    """for x in lista:
        if num1 in lista:
            sum+=1"""
    for x in lista:
        if not in repetidos:
            repetidos.append(x)
    else:
        print('esta repetido')