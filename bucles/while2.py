# este programa me dice si dos numero son factores, si no lo son se repite el ciclo
# se declaran las variables con valores que cumplen la condicion para que pueda iniciar el ciclo
x=5
y=3


# inicio del bloque de codigo del ciclo while, donde se que la condicon es que si no son factores se repite  
# el operador mod (%) me muestra el residuo de una division, si es diferente a cero entonces pide los numeros nuevamente 
# si el residuo es cero entonces es factor y se acaba el ciclo 
while not (x%y==0 or y%x==0): # se deben cumplir una o dos de las condiciones 
    print('Rutina para saber si dos numeros son factores')
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))    
print('Son factor')