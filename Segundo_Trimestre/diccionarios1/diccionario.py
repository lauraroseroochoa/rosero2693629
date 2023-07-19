diccionario={'azul': 'blue',
             'rojo': 'red',
             'amarillo': 'yellow',
             'verde': 'green',
             'rosado': 'pink',
             'morado':'pruple',
             'naranja':'orange',
             'negro':'black',
             'blanco':'white',
             'cafe':'brown',}
print(diccionario)
words=['rosado', 'gris', 'salmon','cafe']

for i in words:
    if i in diccionario:
        print(i, '=', diccionario[i])
    else:
        print(i,'no esta en el diccionario')
        
        
        
        
        
        
        
        
        
        
def dicc_spanish_english(diccionario):
       dictionary = {'gato': 'cat', 
                     'perro': 'dog', 
                     'mariposa': 'butterfly',
                     'fly': 'mosca', 
                     'oso': 'bear', 
                     'cerdito': 'pig', 
                     'pez': 'fish', 
                     'pajaro': 'bird',}
       diccionario=dictionary
       return diccionario

def dicc_english_spanish(diccionario):
       dictionary_ingles = {'cat':'gato', 
                     'dog': 'perro', 
                     'butterfly':'mariposa',
                     'fly':'mosca', 
                     'bear':'oso', 
                     'pig':'cerdito', 
                     'fish':'pez', 
                     'bird':'pajaro',}
       diccionario=dictionary_ingles
       return diccionario