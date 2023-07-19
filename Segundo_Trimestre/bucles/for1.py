#La estructura de control for ejecuta un bloque de codigo de forma repetitiva  
for i in range(11): # Para una variable en este caso muestra los numeros del cero al 10
    print(i) # La variable muestra la serie un numero antes del que se ingresa como fin
            # inicia desde cero por defecto ya que no se especifico
    
for j in range(1,11): # En este ciclo la variable tiene un nombre diferente y termina un numero antes del once
    print(j)          # inicia desde uno por que es el valor inicial asignado

for k in range(0,11,2): # la serie muestra los numeros pares que hay entre el 0 y el 10 
    print(k) # el tercer valor que es el dos es la cantidad en que incrementa 
    
for i in range(10,-1,-2): # la serie muestra los numeros pares del cero al diez pero de forma descendente 
    print(i)              # el rango asignado del 10 al -1 para que termine un numero antes 
