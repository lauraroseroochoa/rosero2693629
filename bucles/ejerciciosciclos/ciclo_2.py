divisor=[]
num = int(input("Ingrese un numero: "))
x=0
cont=0

for i in range (1,num+1):
    if  num%i==0:
        divisor.append(i)
        cont+=1
if cont<=2:
    print('es primo')
else:
    print('no es primo')
print(f'los divisores del numero son: {divisor}')
print('el numero de divisores',cont)
