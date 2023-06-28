list_regionales = ['bolivar, cundinamarca, antioquia, cladas, quindio, tolima, boyaca, santander, san andres']
def lista_regionalesSena (lista:list):
    while True:
        try:
            regional = input("Digita un elemento: ")
            if not (regional in lista):
                lista.append(regional)
                print(f"Valor aceptado : {lista}")
                if regional == "0":
                    del lista[-1]
                    break
            else:
                raise ValueError (f"Error: Imposible añadir elementos duplicados ")
        except Exception as e:
          print(f"Error {e}")
        except ValueError:
          print('Solo puede ingresar numeros no repetidos')
          print(f'La lista no se actualizo: {lista}')
        except KeyboardInterrupt:
          print('Se interrumpio la ejecucion')
        finally:
          print("Gracias por usar este programa")

    



def mayusculalist(list_regionales):
    lista = []
    for i in list_regionales:
        mayus = i.upper()
        lista.append (mayus)
    return lista

lista_regionalesSena(list_regionales)
list_regionales= mayusculalist(list_regionales)
print(list_regionales)