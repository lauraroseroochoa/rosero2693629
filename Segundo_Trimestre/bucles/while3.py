#rutina para ingresar numeros 
#contar la cantidad de numeros ingresados
#sumar los numeros ingresados entre  si
#hallar el promedio entre los numeros que se ingresaron
#mostrar el numero mayor y menor entre los numeros ingresados
#el ciclo se detiene cuando se ingresa el numero cero y muestra los resultados

# se declaran las variables antes del ciclo
num=1
cont=0
sum=0
num_mayor=0
menor=100000 # debemos asignar un valor grande 

while num!=0: #inicio de ciclo while donde la condicion es que si el numero es diferente a cero se repite el ciclo y si termina hasta ingresar 0
    num=int(input('ingrese numero: '))
    cont=cont+1#cont+=1
    sum+=num
    if num>num_mayor: # inicio de la condicion para que identifique si el numero ingresado es mayor que cero
      num_mayor = num
    if num<menor and num!=0: # inicio de la condicion para identificar que el numero es menor del que se le asigno 
      menor = num
      
cont-=1 # se debe restar uno al contador para que no tenga en cuenta el numero cero que se ingresa al final
prom= (sum)/cont # operacion para conocer el promedio, se divide el resultado de la suma entre la cantidad de numeros
print(f'El usuario ingreso {cont} numeros')
#print('El usuario ingreso', cont, 'numeros')
print(f'la suma de los numeros es {sum}')
print(f'el promedio de los numeros es: {prom}')
print(f'el numero mayor es {num_mayor}')
print(f'el numero menor es {menor}')