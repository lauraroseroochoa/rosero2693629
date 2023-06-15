# verificar numeros de una lista con try - except
numeros =[4,7,6,8,9]

while True:
    try:
        nuevo=int(input('Escriba un numero: '))
        if not (nuevo in numeros):
            numeros.append(nuevo)
            print(f'Valor aceptado : {numeros}')
            break
        else:
            raise ValueError('solo numeros sin repetición')
        
    except ValueError:
        print('Solo puede ingresar numeros no repetidos')
        print(f'La lista no se actualizo: {numeros}')
    except KeyboardInterrupt:
        print('Se interrumpio la ejecucion')