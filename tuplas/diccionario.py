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