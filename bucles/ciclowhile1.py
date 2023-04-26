# esste programa  muestra la suma de los numeros del 1 al 10
i=1 #   se declara la variable 
sum=0
while i<=10: # aqui inicia el bloque de codigo para del ciclo while, la variable debe ser menor o igual a 10
    print(i)
    sum+=i #sum=sum+i # son dos variables que indican la suma que se hace entre los valores de i 
    i+=1 #i=i+1 # se encuentra una variable y una constante y hace que aumente de uno en uno
print('la suma es:',sum)

# este ciclo debe mostrar la suma de los numeros pares y de los impares que estan de 1 a 10
# se declaran las variables en cero
i=0
sp,si=0,0
while i<=10: # inicia el bloque de codigo del ciclo
    print(i)
    if i%2==0: # inicia el bloque de la condicion if para evaluar la igualdad
        sp+=i # si se cumple la condicon anterior es un numero par
    else: # si no se cumple entonces es impar
        si+=i 
    i+=1 # aumenta la variable de uno en uno dependiendo 
print('la suma de los pares es:',sp) # se muestra el total de la suma de los pares
print('la suma de los impares es:',si) # se muestra el total de la suma de los impares