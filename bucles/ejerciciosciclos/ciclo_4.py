divisor=[]
num = 1001
x=0
cont=0
suma=0
cont2=0
for i in range (1,num):
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