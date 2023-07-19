# Programa que le pida al usuario 
inicio = int(input('Ingrese un numero inicial para la serie: '))
fin = int(input('Ingrese numero en el que desea finalizar: '))
cantidad= int(input('ingrese un numero positivo para incrementar o para decrementar: '))
for i in range (inicio,fin,cantidad):
     print (i)