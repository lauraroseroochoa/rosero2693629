# Hacer una lista que sea de un rango aleatoria de mínimo 15, máximo 125
# si la lista generada no es múltiplo de 5 el programa debe de generar otra hasta que salga una de múltiplo de 5.
# Los datos de la lista se representan con float ya que se quiere dar una estatura
# el rango de los números es de 1,50 hasta 2,00
# El programa tiene que hallar los quintiles
# además de hallarlos tiene que imprimir el rango 

import random
def llenarLista(tam,rango):
    tam1=random.randint(15,tam)
    while tam1==tam1:
        tam1=random.randint(15,tam)
        if tam1%5==0:
            lista=[round(random.uniform(1.50,rango),2) for i in range(tam)]
            return lista
        
def ordenarListaAsc(lista):
    for i in range(len(lista)):
        for j in range(i+1,(len(lista))):
         if lista[i]>lista[j]:
             aux=lista[i]
             lista[i]=lista[j]
             lista[j]=aux
    return lista  

def hallarQuintiles(lista,valor):
    quintil=valor*len(lista)/5
    mayor=int(quintil)
    menor=int((valor-1)*len(lista)/5)
    if len(lista)>quintil:
        listaquin=lista[menor:mayor]
        return listaquin
    else:
        return f'no se puede hallar el quintil'


list=llenarLista(125,1.82)
print(list)
print(ordenarListaAsc(list))
print(len(list))
num=int(input('ingresa el quintil a hallar: '))
print(hallarQuintiles(list,num))