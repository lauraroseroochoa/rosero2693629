# 1. Finaliza el siguiente código con una gestión completa de sus excepciones. 
#  El objetivo del programa es solicitar al usuario una posición de una lista y devolver el valor que se encuentra en dicha posición. 
#  Prueba el programa enviando una posición inexistente y enviando una letra como posición. 
#  El programa sólo terminará cuando se ejecute correctamente   

try:
    lista = [3,5,6,8]
    pos = int(input("ingrese la posición del elemento que desea obtener:"))
    print(f"El valor en la posicion {pos} es {lista[pos]}")
except IndexError as i:
    print("El numero de la posicion no se encuentra en la lista")