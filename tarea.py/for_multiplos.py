# Programa que solicite un numero positivo al usuario
# Diga cuantos multiplos de un numero hay en la serie
# Desde cero hasta el numero ingresado

fin = int(input('Ingrese numero en el que desea finalizar: '))
cantidad= int(input('ingrese un numero positivo para incrementar o uno negativo para decrementar: '))
for i in range (0,fin,cantidad):
     print (i)
num = int(input('Ingrese un numero positivo: '))
while num<=0:
     num = int(input('Ingrese un numero positivo: '))

n=0
for x in range (fin+1):
    if x%num==0:
         n+=1
print(f'los multiplos de el numero ingresado son:{n-1}')