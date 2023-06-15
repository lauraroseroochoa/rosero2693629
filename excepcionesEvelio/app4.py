""" Lista_pares. Números pares (Validar con código que lo sean a medida que se digitan)
Función lista_pares() """

list_par = []
list_multiplos = []

def pares (lista:list):
    while True:
        try:
            nuevo = int(input("Escriba un numero: "))
            if not (nuevo in lista):
                if nuevo % 2 == 0:
                    lista.append(nuevo)
                    print(f"Valor aceptado: {lista}")
                    if nuevo == 0:
                        break
            else:
                raise ValueError("Solo numeros que sean pares")
    
        except ValueError:
            print("Solo puedes ingresar numeros pares")
            print(f"La lista no se actualizao {lista}")
        except KeyboardInterrupt:
            print("Se interrumpio la ejecucion")

def Multiplos (lista:list):
    while True:
        try:
            nuevo = int(input("Escriba un numero: "))
            if not (nuevo in lista):
                if nuevo % 4 == 0:
                    lista.append(nuevo)
                    print(f"Valor aceptado: {lista}")
                    if nuevo == 0:
                        break
            else:
                raise ValueError("Solo numeros mmultiplos de 4 y que no esten repetidos")
    
        except ValueError:
            print("Solo puedes ingresar numeros que sean multiplos de 4")
            print(f"La lista no se actualizao {lista}")
        except KeyboardInterrupt:
            print("Se interrumpio la ejecucion")


pares (list_par)
Multiplos (list_multiplos)