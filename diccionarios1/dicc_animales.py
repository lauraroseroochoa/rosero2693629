
   
def agregar_spanish(diccionario,x,y):
    #diccionario=dicc_spanish_english(diccionario)
    #while x or y !=0:
    diccionario.update({x:y})
    #return diccionario

def agregar_english(diccionario,x,y):
    #diccionario=dicc_english_spanih_english(diccionario)
    #while x or y !=0:
    diccionario.update({x:y})
    #return diccionario
    
def usar_dictionary1(diccionario,i):
        if i in diccionario:
          return i, diccionario[i]
        else:
          return i,'no esta en el diccionario'

def usar_dictionary2(diccionario,i):
        if i in diccionario:
          return i, diccionario[i]
        else:
          return i,'no esta en el diccionario'


dictionary={}
dictionary_ingles={}
#print(dicc_spanish_english(dictionary))
#print(dicc_english_spanish(dictionary_ingles))
#clave=str(input('palabra en español que quiere agregar'))
#valor=str(input('palabra en ingles que quiere agregar'))
#print(agregar_spanish(dictionary,clave,valor))

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
            print(dictionary)

        case 4:
            print('.....',dictionary)
            clave=(input('palabra en ingles que quiere agregar: '))
            valor=(input('palabra en español que quiere agregar: '))
            print(agregar_english(dictionary_ingles,clave,valor)
        case 5:
            i=input('ingresa la palabra que quieres traducir: ')
            print(usar_dictionary1(dictionary, i))
        case 6:
            i=input('ingresa la palabra que quieres traducir: ')
            print(usar_dictionary2(dictionary_ingles, i))



