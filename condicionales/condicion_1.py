# en este codigo se ingresan dos numeros por teclado
# se debe saber si estan de forma ascendente, descendente o sin son iguales 
x=input('ingrese numero') 
y=input('ingrese numero')
#inicia el bloque de codigo para la condicion
if x==y: #se evalua sin son iguales los numeros ingresados
    print('son iguales')
elif x>y: # si no se cumple la condicon anterior entonces evalua si es mayor el primer numero
    print('descendente')
else: # si no es mayor entonces no se cumple la condicion y es menor, es decir que esta de forma ascendente
    print('ascendente')