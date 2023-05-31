# ejercicio 8
x=int(input("ingresa un numero: "))
y=int(input("ingresa un numero: "))

def max_com_div(x,y):
    while y!=0:
     z=x%y
     x=y
     y=z
    return x

print("el maximo comun divisor es:")
print(max_com_div(x,y))