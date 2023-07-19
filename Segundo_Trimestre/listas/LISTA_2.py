# Introduccion a listas
# Metodos y funciones que se pueden usar con las listas en Python
x=100 # Se incia una variable 
print('tipo de x',type(x)) # con la funcion type podemos visualizar el tipo de dato que es la variable x (entero)
lista=[1,1.4,'sena',['a','b',],'soacha'] # Se crea la lista con diferentes tipos de  datos como decimales, enteros, cadenas y una sublista
print(f'elemento {lista[4]}') # Dentro print entre los corchetes se llama la lista con uno de los indices para que se muestre solo este elemento en pantalla
print(len(lista)) # con la funcion len podemos mostrar en pantalla la longitud de la lista es decir el numero de elementos que contiene
print('tipo de lista',type(lista)) # con la funcion type podemos visualizar los tipos de datos que estan en la lista
print('ultimo indice',lista[-1]) # en las listas tambien se pueden usar valores negativos para mostrarlos en pantalla, el -1 es el ultimo elemento de la lista

print(len(lista)) # Longitud de la lista
# Los metodos se diferencian de la funcion por el punto con el que se separa
lista.append(20) # Con el metodo append se agrega un elemento al final de la lista 
lista.append('python') 
print(lista)
lista.insert(len(lista),'java') # con el metodo insert se puede insertar un elemento a la lista declarando su posicion y luego el elemento, en este caso se agregara al final de la lista ya que se usa len
print(lista)