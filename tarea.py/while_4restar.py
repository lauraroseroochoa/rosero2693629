# Programa para pedir dos numeros verificar si hay uno mayor que el otro o si no perdilos nuevamente
# Restar el menor del mayor y asi hasta que no se pueda restar mas 
# Mostrar cuanto sobra
resta = 0
num1,num2 = 0,0

# Primero con el ciclo while voy a verificar que un numero de los ingresados sea mayor que el otro  
while (not(num1>num2 or num2>num1)): # La condicion me dice que si en los numeros no hay uno mayor debe pedirlos nuevamente 
    if num1==num2:
        print('Ingrese los numeros a restar')
    num1=int(input('Ingrese un numero: '))
    num2=int(input('Ingrese un numero: '))

    if num1>num2:
        resta=num1-num2
        print(resta)
        while resta>num2:
            resta=resta-num2
            print(resta)
    else:
        resta=num2-num1
        print(resta)
        while resta>num1:
            resta=resta-num1
            print(resta)

print(f'Resultado de la resta: {resta}')
