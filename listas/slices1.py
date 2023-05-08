import random

tam=(random.randint(5,10))
lista=[(random.randrange(100))for i in range (tam)]
rebanada=lista[len(lista)//2:tam] #tam incluye hasta el ultimo dato de la lista, tamben lo puedo dejar en blaco
rebanada2=lista[:]
print(lista)
print(rebanada)
print(rebanada2)