x=int(input("ingresa un numero: "))
y=int(input("ingresa un numero: "))
while y!=0:
    z=x%y
    x=y
    y=z
    
print("el maximo comun divisor es:",x)