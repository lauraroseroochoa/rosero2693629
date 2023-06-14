# 2. Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

def agregar_una_vez (lista:list , element:int):
    try:
        if element in lista:
            raise ValueError (f"Error: Imposible añadir elementos duplicados => {element}.")
        else:
            lista.append(element)
            return lista
    except Exception as e:
        print(f"Error {e}")
    finally:
        print("Gracias por usar este programa")

        
x = 1
list = ['python, javascript, java, typescript, c, c++']
while x !=0 :
    x = int(input("Digita un elemento: "))
    agregar_una_vez(list , x)

    def mayusculalist(list,case):
        lower='abcdefghijklmnopqrstuvwxyz'
        upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        text=''
        for p in list:
            a=0;
            for i in lower:
                if case=='lower':
                    if lower[a]== p or upper[a]==p:
                        text+=lower[a]
                if case=='upper':
                    if upper[a]==p or lower[a]==p:
                        text+=upper[a]
                a+=1
        return text
    
print(mayusculalist(list,'upper'))