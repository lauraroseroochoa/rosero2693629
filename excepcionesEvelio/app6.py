lista = []

def abecedario (listas:list):
    lista_abe = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" ,  "x" , "y" , "z"]
    while True:
        try:
            nuevo = input("Escriba una letra: ")
            if nuevo in lista_abe:
                if not (nuevo in listas):
                    listas.append(nuevo)
                    print(f"Valor aceptado: {listas}")
            elif nuevo == "0":
                break
            else:
                raise ValueError("Solo letras que sean del abecedario")
    
        except ValueError:
            print("Solo puedes ingresar letras del abecedario")
            print(f"La lista no se actualizao {listas}")
        except KeyboardInterrupt:
            print("Se interrumpio la ejecucion")
        finally:
            print("Gracias por usar este programa")

abecedario(lista)