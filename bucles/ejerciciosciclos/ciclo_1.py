divisor=[]
num = int(input("Ingrese un numero: "))
x=0
for i in range (1,num+1):
    if  num%i==0:
        divisor.append(i)
print(f'los divisores del numero son: {divisor}')