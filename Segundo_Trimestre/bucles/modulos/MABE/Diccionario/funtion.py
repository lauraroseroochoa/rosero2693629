def alimentar_diccionario_esp_ingles(diccionarioI):
    palabra_esp = input("Ingrese una palabra en español: ")
    palabra_ing = input("Ingrese la traducción de la palabra en inglés: ")
    diccionarioI[palabra_esp] = palabra_ing
    return diccionarioI


def alimentar_diccionario_ingles_esp(diccionarioE):
    palabra_ing = input("Ingrese una palabra en inglés: ")
    palabra_esp = input("Ingrese la traducción de la palabra en español: ")
    diccionarioE[palabra_ing] = palabra_esp
    return diccionarioE

def usar_diccionario_esp_ingles(diccionarioI):
    palabra_esp = input("Ingrese una palabra en español para buscar su traducción: ")
    if palabra_esp in diccionarioI:
        print("La traducción al inglés es:", diccionarioI[palabra_esp])
    else:
        print("La palabra no se encuentra en el diccionario.")


def usar_diccionario_ingles_esp(diccionarioE):
    palabra_ing = input("Ingrese una palabra en inglés para buscar su traducción: ")
    if palabra_ing in diccionarioE:
        print("La traducción al español es:", diccionarioE[palabra_ing])
    else:
        print("La palabra no se encuentra en el diccionario.")
