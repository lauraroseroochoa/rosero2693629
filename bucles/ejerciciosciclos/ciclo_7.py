# ejercicio 7
num_positive=1
mayor=0
cont=0
while num_positive>0:
    num_positive=int (input("ingresa un numero: ")) 
    cont+=1
    if num_positive<0:
        print("el numero es negativo")
cont-=1
print("la cantidad de numeros positivos ingresados es:",cont)
print(num_positive)