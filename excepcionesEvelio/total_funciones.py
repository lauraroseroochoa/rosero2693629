# 2. Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

print('ingresando el numero 0 finalizaras una funcion y empezara la otra')

def mayusculalist(list):
    lista = []
    for i in list:
        mayus = i.upper()
        lista.append (mayus)
    return lista
 
list_lenguajes = ['python, javascript, java, typescript, c, c++']
def list_lenguajes_programacion (lista:list):
    while True:
        try:
            x = input("Ingresa un lenguaje de programacion: ")
            if not (x in lista):
                lista.append(x)
                print(f"Valor aceptado : {lista}")
                if x == "0":
                    del lista[-1]
                    break
            else:
                raise ValueError (f"Error: Imposible añadir elementos duplicados ")
        
        except ValueError:
            print('Solo puede ingresar numeros no repetidos')
            print(f'La lista no se actualizo: {lista}')
        except KeyboardInterrupt:
            print('Se interrumpio la ejecucion')
        except Exception as e:
          print(f"Error {e}")
        finally:
            print("Gracias por usar este programa")



list_lenguajes_programacion(list_lenguajes)
list_lenguajes = mayusculalist(list_lenguajes)
print(list_lenguajes)


print('lista de regionales del sena')
# lista de nombres de regionales sena

list_regionales = ['Centro del diseño y manufactura del cuero -Itagui-, Centro de los recursos naturales renovables la salada -Caldas-, Centro para el desarrollo del habitat y construccion -Medellín-, Centro tecnologico del mobiliario, Centro internacional nautico, Centro minero -Morca-, Centro tecnologico de la amazonia -Florencia']
def lista_regionalesSena (lista:list):
    while True:
        try:
            regional = input("Ingresa el nombre de una regional sena: ")
            if not (regional in lista):
                lista.append(regional)
                print(f"Valor aceptado : {lista}")
                if regional == "0":
                    del lista[-1]
                    break
            else:
                raise ValueError (f"Error: Imposible añadir elementos duplicados ")
        
        except ValueError:
          print('Solo puede ingresar numeros no repetidos')
          print(f'La lista no se actualizo: {lista}')
        except KeyboardInterrupt:
          print('Se interrumpio la ejecucion')
        except Exception as e:
          print(f"Error {e}")
        finally:
          print("Gracias por usar este programa")

    
lista_regionalesSena(list_regionales)
list_regionales= mayusculalist(list_regionales)
print(list_regionales)

print('funcion pares')
""" Lista_pares. Números pares (Validar con código que lo sean a medida que se digitan)
Función lista_pares() """

list_par = []
list_multiplos = []

def pares (lista:list):
    while True:
        try:
            nuevo = int(input("Escriba un numero: "))
            if nuevo != 0:
                if not (nuevo in lista):
                    if nuevo % 2 == 0:
                        lista.append(nuevo)
                        print(f"Valor aceptado, si es par: {lista}")
                    
            else:
                if nuevo == 0:
                        break
                raise ValueError("Solo numeros que sean pares")
    
        except ValueError:
            print("Solo puedes ingresar numeros pares")
            print(f"La lista no se actualizao {lista}")
        except KeyboardInterrupt:
            print("Se interrumpio la ejecucion")
            
pares (list_par)

print('funcion multiplos de 4')

def Multiplos (lista:list):
    while True:
        try:
            nuevo = int(input("ingresa un numero multiplo de cuatro: "))
            if nuevo != 0:
                if not (nuevo in lista):
                    if nuevo % 4 == 0:
                        lista.append(nuevo)
                        print(f"Valor aceptado, si es multiplo de 4: {lista}")
                    
            else:
                if nuevo == 0:
                        break
                raise ValueError("Solo numeros mmultiplos de 4 y que no esten repetidos")
    
        except ValueError:
            print("Solo puedes ingresar numeros que sean multiplos de 4")
            print(f"La lista no se actualizao {lista}")
        except KeyboardInterrupt:
            print("Se interrumpio la ejecucion")


Multiplos (list_multiplos)

print('nombres de aprendices de la ficha')
# lista nombre de los aprendices de la ficha

list_curso= []
def nombres (lista:list):
    while True:
        try:
            nuevo = input("Digite el nombre de un aprendiz de su ficha: ")
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


nombres(list_curso)
list_curso = mayusculalist(list_curso)
print(list_curso)


print('lista que solo permite letras')
# lista que solo permite letras

lista_solo_letras = []

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

abecedario(lista_solo_letras)


def imprimir_listas():
    print(list_lenguajes)
    print(list_regionales)
    print(list_par)
    print(list_multiplos)
    print(list_curso)
    print(lista_solo_letras)
    
print(imprimir_listas())