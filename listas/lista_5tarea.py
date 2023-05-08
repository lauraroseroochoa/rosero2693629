# serie fibonachi
def fibo(z):
    num1=0
    num2=1
    for x in range(z):
        num3 = num1 + num2
        num1= num2
        num2= num3
    return num2

num1=int(input('ingrese el numero que define la cantidad numeros para la serie: '))
lista=[]
for b in range(num1):
    lista.append(fibo(b))
print(lista)        