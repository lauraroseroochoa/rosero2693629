# ejercicio 3
divisor=[]
num = int(input("Ingrese un numero: "))
x=0
cont=0
suma=0
for i in range (1,num+1):
    if  num%i==0:
        divisor.append(i)
        cont+=1
        suma+=i

if cont<=2:
    print('es primo')
else:
    print('no es primo')
print(f'los divisores del numero son: {divisor}')
print('el numero de divisores es:',cont)
print('el resultado de la suma',suma-num)
if suma-num==num:
    print(f'{num} Es un numero perfecto')
else:
    print('no es perfecto',suma-num)