def usarEspañol (diccionario , x):
    if x in diccionario:
        return diccionario[x]

def usarIngles (diccionario , x):
    if x in diccionario:
        return diccionario[x]

def updateEspañol(diccio , x , y):
    diccio.update({x : y})
    return diccio

def updateIngles(diccio , x , y):
    diccio.update({x : y})
    return diccio