# llenar un tupla con n elemento max 20 y numeros entre 0 y 100
# sumar los elementos de la tupla
import random
tupla=()
tam=int(random.randrange(20))

for i in range(tam):
    numeros=random.randrange(100)
    tupla=tupla+(numeros,)
print(tupla)
print(tam)