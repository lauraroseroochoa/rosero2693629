def agregar_spanish(diccionario,x,y):
    diccionario.update({x:y})
    


def agregar_english(diccionario,x,y):
    diccionario.update({x:y})
    
    
    
def usar_dictionary(diccionario,i):
        if i in diccionario:
          return i, diccionario[i]
        else:
          return i,'no esta en el diccionario'

def usar_dictionary(diccionario,i):
        if i in diccionario:
          return i, diccionario[i]
        else:
          return i,'no esta en el diccionario'

def guardartuplaespañol(tupla,x):
    tupla=tupla +(x,)
    return tupla


def guardartuplaingles(tupla,x):
    tupla=tupla+(x,)
    return tupla


dictionary={}
dictionary_ingles={}
diccionario_español={}
diccionario_ingles={}


print('1. diccionario español ingles')
print('2. diccionario ingles español')
print('3. agregar nueva palabra al diccionario de español')
print('4. agregar nueva palabra al diccionario de ingles')
print('5. usar diccionario español')
print('6. usar diccionario ingles')


s=int(1)
while s!=0:
    s=int(input('selecciona una opcion'))
    match s:
        case 1: 
           print(dictionary)
        case 2:
           print(dictionary_ingles)
        case 3:
            print('.....',dictionary)
            clave=(input('palabra en español que quiere agregar: '))
            valor=(input('palabra en ingles que quiere agregar: '))
            agregar_spanish(dictionary,clave,valor)       
            diccionario_español=guardartuplaespañol(diccionario_español,clave)
            print(dictionary)

        case 4:
            print('.....',dictionary)
            clave=(input('palabra en ingles que quiere agregar: '))
            valor=(input('palabra en español que quiere agregar: '))
            agregar_english(dictionary_ingles,clave,valor)
            diccionario_ingles=guardartuplaingles(diccionario_ingles,clave)
            print(dictionary_ingles)
            
        case 5:
            i=input('ingresa la palabra que quieres traducir: ')
            print(usar_dictionary(dictionary, i))
        
        case 6:
            i=input('ingresa la palabra que quieres traducir: ')
            print(usar_dictionary(dictionary_ingles, i))







