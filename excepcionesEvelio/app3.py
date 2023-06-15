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

        
regional = 1
list_regionales = ['python, javascript, java, typescript, c, c++']

while regional != "0" :
    regional = input("Digita un elemento: ")

    agregar_una_vez(list_regionales , regional)

    def mayusculalist(list_regionales):
        lista = []
        for i in list_regionales:
            mayus = i.upper()
            lista.append (mayus)
            del list_regionales[-1]
        return lista

print(mayusculalist(list_regionales))