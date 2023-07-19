# llenar una lista con numeros aleatorios (reales con un decimal) que representen calificaciones de un curso
# Se evalua de 0 a 5
# El curso puede tener entre 20 y 30 aprendices
# Hallar 
# Genere listas nuevas para los aprobados y reprobados (se aprueba con 3)
# Genere listas nuevas por cada unidad. los que sancan  de  1 a 0 son un grupo
# Los de 1 a 2 otro grupo y asi sucesivamente
# Diga cual es el promedio de los que aprueban y de los que repruebban por separado

import random

suma_reprobados=0
tam=(random.randint(20,30))
print(f'{tam} estudiantes')
lista=[float(random.randrange(6))for i in range (tam)]
print(lista)
for i in range(len(lista)):
    for z in range (i+1,len(lista)):
     if lista[i]>lista[z]:
        aux=lista[i]
        lista[i]=lista[z]
        lista[z]=aux
print(lista)

for j in lista:
    if j<=3.0:
        posicion=(lista.index(j))
    if j==2.0:
        unidad1=(lista.index(j))
    if j==4.0:
        unidad2=(lista.index(j))  
        
posicion1=lista[:unidad1]   
posicion2=lista[unidad1:unidad2]  
posicion3=lista[unidad2:]     

for i in lista:
    if i<3.0:
        suma_reprobados+=i
promedio=suma_reprobados/2        
  
print('el numero esta en la posicion',posicion)
aprobaron=lista[posicion]
reprobaron=lista[:posicion]
print('aprobados',aprobaron)
print('reprobados',reprobaron)
print('notas unidad 1',posicion1)
print('notas unidad 2',posicion2)
print('notas unidad 3',posicion3)
#print(suma_reprobados)
print('promedio',promedio)