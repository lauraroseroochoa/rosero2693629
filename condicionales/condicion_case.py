#Este programa es para realizar diferentes operaciones entre dos numeros 
#dependiendo de la opcion que se ingrese por teclado
num1,num2=100,25 # se declaran las variables asignandoles un valor

# con print se muestran en la pantalla las diferentes opciones
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
selector=(input('Digite la opcion')) # en la variable selector se almacena la opción seleccionada por el usuario
match selector: # inicio de bloque de matchcase 
    case '1': #En el primer caso está la opción de sumar los numeros 
        print(num1+num2)
    case '2': #En el segundo caso está la opción de restar los numeros
        print(num1-num2)
    case '3': #En el tercer caso está la opción de multiplicar los numeros 
        print(num1*num2)
    case '4': #En este último caso se dividen los numeros
        print(num1/num2)
