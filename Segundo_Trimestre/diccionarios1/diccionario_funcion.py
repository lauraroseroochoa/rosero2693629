def existepalabra(diccionario,word):
    if word in diccionario:
        return diccionario[word]
    else:
        return f'la palabra {word} no esta en el diccionario'
    
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

word= input("digita un color en español: ")   
print(existepalabra(diccionario,word))