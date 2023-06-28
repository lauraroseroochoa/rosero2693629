lista= []
def nombres (lista:list):
    while True:
        try:
            nuevo = input("Digite un nombre: ")
            if not (nuevo in lista):
                lista.append(nuevo)
                print(f"Valor aceptado : {lista}")
                if nuevo == "0":
                    del lista[-1]
                    break
            else:
                raise ValueError("Solo nombres de la ficha 2693629")
        
        except ValueError:
            print("solo puede ingresar nombres de la ficha 2693629")
            print(f"la lista no se actualizo {lista}")
        except KeyboardInterrupt:
            print ("se interrumpio la ejecucion")

def mayusculalist(list):
    lista = []
    for i in list:
        mayus = i.upper()
        lista.append (mayus)
    return lista


nombres(lista)
# print(mayusculalist(lista))
lista = mayusculalist(lista)
print(lista)