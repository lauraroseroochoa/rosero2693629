# ejercicio 2
num = int(input("Ingrese un numero: "))

def primo(num):
    divisores=[]
    cont=0
    for i in range (1,num+1):
        if  num%i==0:
            divisores.append(i)
            cont+=1     
    if cont<=2:
        return'es primo'
    else:
        return'no es primo'
    

print(primo(num))
