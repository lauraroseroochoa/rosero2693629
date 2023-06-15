# 2. Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

def agregar_una_vez (lista:list , element:str):
    try:
        if element in lista:
            raise ValueError (f"Error: Imposible añadir elementos duplicados => {element}.")
        else:
            lista.append(element)
            return lista
    except Exception as e:
        print(f"Error {e}")
    except ValueError:
        print('Solo puede ingresar numeros no repetidos')
        print(f'La lista no se actualizo: {lista}')
    except KeyboardInterrupt:
        print('Se interrumpio la ejecucion')
    finally:
        print("Gracias por usar este programa")

        
x = 1
list_lenguajes = ['python, javascript, java, typescript, c, c++']

while x != "0" :
    x = input("Digita un elemento: ")

    agregar_una_vez(list_lenguajes , x)

def mayusculalist(list_lenguajes):
    lista = []
    for i in list_lenguajes:
        mayus = i.upper()
        lista.append (mayus)
        del list_lenguajes[-1]
    return lista

print(mayusculalist(list_lenguajes))